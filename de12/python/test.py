from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

# 使用 m2m100 模型
model_name = "facebook/m2m100_418M"
tokenizer = M2M100Tokenizer.from_pretrained(model_name)
model = M2M100ForConditionalGeneration.from_pretrained(model_name)

# 输入文本
text = "Hello, world"

# 编码输入
inputs = tokenizer(text, return_tensors="pt")

# 生成翻译
translated = model.generate(**inputs)

# 解码翻译
translation = tokenizer.decode(translated[0], skip_special_tokens=True)
print(translation)
