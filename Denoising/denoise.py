
import torch
from torchvision.models import VGG19_BN_Weights
#model = resnet18
model=torch.load('skin/model.pth',map_location='mps')
weights = torch.load('skin/weights.pth',map_location='mps')
model.load_state_dict(weights)
skin_map={0:'Добро',1:'Зло'}
def get_evil(img):
    
    transform = VGG19_BN_Weights.IMAGENET1K_V1.transforms()
    
    input_image = transform(img).unsqueeze(0) # Добавьте размерность пакета (batch dimension)
    
    device = torch.device("cuda" if torch.cuda.is_available() else 'mps')
    model.to(device)
    model.eval()
    input_image = input_image.to(device)
    #model.to(device)
    res=model(input_image).item()
    return f'Степень злобы: {res}\n\n Т.е. опухоль: {skin_map[round(res)]}'