import torch
import torchvision
import torchvision.transforms as transforms
from transformers import ResNetForImageClassification
from tqdm import tqdm  # 进度条显示
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # 调整图像形状和通道
    transforms.Grayscale(num_output_channels=3),  
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  
])
test_dataset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=32, shuffle=False)
model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")
model.eval()
correct = 0
total = 0
with torch.no_grad():  
    for images, labels in tqdm(test_loader, desc='Processing', unit='batch'):
        outputs = model(images).logits 
        predicted =outputs.argmax(-1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
accuracy = 100 * correct / total
print(f'Accuracy on MNIST test set: {accuracy:.2f}%')