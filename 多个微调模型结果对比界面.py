import gradio as gr
from openai import OpenAI

# 这里填写实际的MODEL_NAME和openai.api_key
MODEL_NAME_1 = "your-model-name"
MODEL_NAME_2 = "your-model-name"
MODEL_NAME_3 = "your-model-name"
MODEL_NAME_4 = "your-model-name"
MODEL_NAME_5 = "your-model-name"

client = OpenAI(api_key="your-openai-api-key")

def translate(input_text):
    responses = []
    for model_name in [MODEL_NAME_1, MODEL_NAME_2, MODEL_NAME_3, MODEL_NAME_4, MODEL_NAME_5]:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "你是一名资深翻译家，将汉语的政治文献翻译成俄语。"},# 这里的文本要跟微调时候给到的system设定一致
                {"role": "user", "content": f"请将以下汉语文本翻译成俄语：\n\n{input_text}"}
            ],
            temperature=0 # 这里可以根据需求适当加大数值
        )
        translated_text = response.choices[0].message.content
        responses.append(translated_text.strip())
    return responses

input_text = gr.Textbox(label="汉语原文", lines=12, placeholder="请输入待翻译的文本…")
output_text_1 = gr.Textbox(label="俄语译文-模型1", lines=3)
output_text_2 = gr.Textbox(label="俄语译文-模型2", lines=3)
output_text_3 = gr.Textbox(label="俄语译文-模型3", lines=3)
output_text_4 = gr.Textbox(label="俄语译文-模型4", lines=3)
output_text_5 = gr.Textbox(label="俄语译文-模型5", lines=3)

gr.Interface(
    fn=translate,
    inputs=input_text,
    outputs=[output_text_1, output_text_2, output_text_3, output_text_4, output_text_5],
    title="汉俄政治文献翻译",
    description="请输入汉语文本，以使用微调过的GPT模型将其翻译成俄语，可点击下方Flag按钮将结果保存到日志。",
).launch(share=True, inbrowser=True)