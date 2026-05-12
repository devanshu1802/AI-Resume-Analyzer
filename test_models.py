import google.generativeai as genai

genai.configure(api_key="AIzaSyAzsZkmpXE75LgLVy6FGlOGiz7oYTkaZMc")

models = genai.list_models()

for model in models:
    print(model.name)