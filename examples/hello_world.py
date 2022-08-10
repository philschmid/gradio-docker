import gradio as gr

# def greet_user(input):
#     return f"Hello, {input}!"


# def main():
#     with gr.Blocks() as app:
#         with gr.Row():
#             with gr.Column():
#                 text_box = gr.Textbox(label="write your name.")
#                 greet_button = gr.Button(value="greet")
#             with gr.Column():
#                 result_box = gr.Textbox(label="result")
#         greet_button.click(fn=greet_user, inputs=text_box, outputs=result_box)
#     app.launch(server_name="0.0.0.0")


# if __name__ == "__main__":
#     main()
    
def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch(server_name="0.0.0.0")