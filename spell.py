import language_tool_python
import spacy

tool = language_tool_python.LanguageTool('en-US')
nlp = spacy.load("en_core_web_sm")

def final_professional_corrector(text):
    print("\n🔍 Analyzing text...\n")

    corrected_text = tool.correct(text)

    matches = tool.check(text)

    if matches:
        print(f"❗ Issues found: {len(matches)}\n")
        for match in matches:
            print(f"- Issue: {match.message}")
            print(f"  ↳ Suggestions: {match.replacements}\n")
    else:
        print("✅ No grammar/spelling/punctuation errors found!\n")

    doc = nlp(text)

    print("\n📌 POS TAGGING:")
    for token in doc:
        print(f"{token.text:15} -> {token.pos_}")

    return corrected_text


if __name__ == "__main__":
    user_input = input("Enter your sentence for professional correction: ")

    if user_input.strip():
        result = final_professional_corrector(user_input)

        print("\n📝 Corrected Output:")
        print(result)
    else:
        print("Please enter a valid sentence.")
