from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from transformers import AutoProcessor, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(r'B:\Playground\LNRS\florence_docvqa-transformers-default-v1\Florence2-DocVQA',trust_remote_code=True).to("cuda").eval()
processor = AutoProcessor.from_pretrained(r'B:\Playground\LNRS\florence_docvqa-transformers-default-v1\Florence2-DocVQA', trust_remote_code=True)

def run_example(task_prompt, image, text_input=None):
    if text_input is None:
        prompt = task_prompt
    else:
        prompt = task_prompt + text_input
    inputs = processor(text=prompt, images=image, return_tensors="pt").to("cuda")
    generated_ids = model.generate(
        input_ids=inputs["input_ids"],
        pixel_values=inputs["pixel_values"],
        max_new_tokens=1024,
        early_stopping=False,
        do_sample=False,
        num_beams=3,
    )
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
    parsed_answer = processor.post_process_generation(
        generated_text,
        task=task_prompt,
        image_size=(image.width, image.height)
    )
    return parsed_answer

def process_image(image, text_input=None):
    # image = Image.open(image)
    image=image.convert("RGB")
    task_prompt = 'What is'
    results = run_example(task_prompt, image, text_input)[task_prompt].replace("<pad>", "")
    return results


def noice(img_path,ques):
    try:
        wrong=process_image(img_path,ques)
        if wrong=='unanswerable':
            return ''
        return wrong
    
    except Exception as e:
        
        print(f"{e}")
        return ''