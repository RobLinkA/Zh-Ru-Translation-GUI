import gradio as gr
from openai import OpenAI

# 这里填写实际的MODEL_NAME和openai.api_key
MODEL_NAME = "your-model-name"
client = OpenAI(api_key="your-openai-api-key")

def translate(input_text):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "你是一名资深翻译家，将汉语的政治文献翻译成俄语。"}, # 这里的文本要跟微调时候给到的system设定一致
            {"role": "user", "content": f"请将以下汉语文本翻译成俄语:\n\n{input_text}\n\n俄语译文:"}
        ],
        temperature=0 # 这里可以根据需求适当加大数值
    )

    translated_text = response.choices[0].message.content
    return translated_text.strip()

input_text = gr.Textbox(label="Input Text", lines=12, placeholder="请输入待翻译的文本…")
output_text = gr.Textbox(label="Translated Text", lines=12)

gr.Interface(
    fn=translate,
    inputs=input_text,
    outputs=output_text,
    title="汉俄政治文献翻译",
    description="请输入汉语文本，以使用微调过的GPT模型将其翻译成俄语。",
).launch(share=True, inbrowser=True)