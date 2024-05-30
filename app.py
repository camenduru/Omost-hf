import gradio as gr
import spaces
import torch

zero = torch.Tensor([0]).cuda()
print(zero.device) # <-- 'cpu' 🤔

@spaces.GPU
def greet(n):
    print(zero.device) # <-- 'cuda:0' 🤗
    return f"Hello {zero + n} Tensor"

demo = gr.Interface(fn=greet, inputs=gr.Number(), outputs=gr.Text())
demo.launch()
