from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "microsoft/phi-2"

print("Téléchargement du modèle...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",   # utilise GPU si dispo
    torch_dtype="auto"
)

print("Modèle chargé !")
