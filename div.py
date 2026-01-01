import streamlit as st

st.set_page_config(page_title="Ancient Names Translator", page_icon="📜")
st.title("📜 Ancient Names Translator")

st.markdown("""
Translate **names or words** between:
- English ↔ Brahmi  
- English ↔ Kharosthi  
- English ↔ Tamil  
- English ↔ Hebrew  
- English ↔ Aramaic  
- English ↔ Greek  
- English ↔ Latin (Old Roman)
""")

# ---------------- BRAHMI ----------------
brahmi_cons = {
    "k":"𑀓","g":"𑀕","c":"𑀘","j":"𑀚",
    "t":"𑀢","d":"𑀤","n":"𑀦",
    "p":"𑀧","m":"𑀫","y":"𑀬",
    "r":"𑀭","l":"𑀮","v":"𑀯",
    "s":"𑀲","h":"𑀳"
}
brahmi_indep_vowels = {
    "a":"𑀅","ā":"𑀆","i":"𑀇","ī":"𑀈",
    "u":"𑀉","ū":"𑀊","e":"𑀏","ai":"𑀐",
    "o":"𑀑","au":"𑀒"
}
brahmi_dep_vowels = {
    "a":"","ā":"𑀸","i":"𑀺","ī":"𑀻",
    "u":"𑀼","ū":"𑀽","e":"𑀾","ai":"𑀿",
    "o":"𑁀","au":"𑁁"
}

# ---------------- KHAROSTHI ----------------
kharosthi_cons = {
    "k":"𐨑","g":"𐨒","c":"𐨓","j":"𐨔",
    "t":"𐨕","d":"𐨖","n":"𐨗","p":"𐨘","b":"𐨙",
    "m":"𐨚","y":"𐨛","r":"𐨜","l":"𐨝","v":"𐨞",
    "s":"𐨟","h":"𐨠"
}
kharosthi_indep_vowels = {
    "a":"𐨀","i":"𐨁","u":"𐨂","e":"𐨃","o":"𐨄"
}
kharosthi_dep_vowels = {
    "a":"","i":"𐨁","u":"𐨂","e":"𐨃","o":"𐨄"
}

# ---------------- TAMIL ----------------
tamil = {"a":"அ","i":"இ","u":"உ","e":"எ","o":"ஒ",
         "k":"க","c":"ச","t":"த","n":"ந","p":"ப","m":"ம",
         "y":"ய","r":"ர","l":"ல","v":"வ","s":"ஸ","h":"ஹ"}
tamil_rev = {v:k for k,v in tamil.items()}

# ---------------- HEBREW ----------------
hebrew = {"a":"א","b":"ב","g":"ג","d":"ד","h":"ה",
          "k":"כ","l":"ל","m":"מ","n":"נ","r":"ר","s":"ש","t":"ת","y":"י","v":"ו"}
hebrew_rev = {v:k for k,v in hebrew.items()}

# ---------------- ARAMAIC ----------------
aramaic = {"a":"𐡀","b":"𐡁","g":"𐡂","d":"𐡃","h":"𐡄",
           "k":"𐡊","l":"𐡋","m":"𐡌","n":"𐡍","r":"𐡓","s":"𐡔","t":"𐡕"}
aramaic_rev = {v:k for k,v in aramaic.items()}

# ---------------- GREEK ----------------
greek = {"a":"Α","b":"Β","g":"Γ","d":"Δ","e":"Ε","z":"Ζ","i":"Ι","k":"Κ","l":"Λ",
         "m":"Μ","n":"Ν","o":"Ο","p":"Π","r":"Ρ","s":"Σ","t":"Τ","u":"Υ"}
greek_rev = {v:k for k,v in greek.items()}

# ---------------- LATIN ----------------
latin = {chr(i): chr(i).upper() for i in range(97,123)}
latin_rev = {v:k for k,v in latin.items()}

# ---------------- FUNCTIONS ----------------
def english_to_brahmi(word):
    result = ""
    i = 0
    word = word.lower()
    while i < len(word):
        if i+1 < len(word) and word[i:i+2] in brahmi_indep_vowels:
            result += brahmi_indep_vowels[word[i:i+2]]
            i += 2
        elif word[i] in brahmi_indep_vowels:
            result += brahmi_indep_vowels[word[i]]
            i += 1
        elif word[i] in brahmi_cons:
            cons = brahmi_cons[word[i]]
            vowel = ""
            if i+2 <= len(word) and word[i+1:i+3] in brahmi_dep_vowels:
                vowel = brahmi_dep_vowels[word[i+1:i+3]]
                i += 2
            elif i+1 < len(word) and word[i+1] in brahmi_dep_vowels:
                vowel = brahmi_dep_vowels[word[i+1]]
                i += 1
            result += cons + vowel
            i += 1
        else:
            result += word[i]
            i += 1
    return result

def english_to_kharosthi(word):
    result = ""
    i = 0
    word = word.lower()
    while i < len(word):
        if i+1 < len(word) and word[i:i+2] in kharosthi_indep_vowels:
            result += kharosthi_indep_vowels[word[i:i+2]]
            i += 2
        elif word[i] in kharosthi_indep_vowels:
            result += kharosthi_indep_vowels[word[i]]
            i += 1
        elif word[i] in kharosthi_cons:
            cons = kharosthi_cons[word[i]]
            vowel = ""
            if i+2 <= len(word) and word[i+1:i+3] in kharosthi_dep_vowels:
                vowel = kharosthi_dep_vowels[word[i+1:i+3]]
                i += 2
            elif i+1 < len(word) and word[i+1] in kharosthi_dep_vowels:
                vowel = kharosthi_dep_vowels[word[i+1]]
                i += 1
            result += cons + vowel
            i += 1
        else:
            result += word[i]
            i += 1
    return result

def to_script(text, mapping):
    return "".join(mapping.get(c.lower(), c) for c in text)

def to_english(text, reverse_map):
    return "".join(reverse_map.get(c, c) for c in text)

# ---------------- UI ----------------
mode = st.selectbox("Choose Translation Mode", ["English → Ancient", "Ancient → English"])
text = st.text_input("Enter text:")

if text:
    if mode == "English → Ancient":
        st.subheader("Translations")
        translations = {
            "Brahmi": english_to_brahmi(text),
            "Kharosthi": english_to_kharosthi(text),
            "Tamil": to_script(text, tamil),
            "Hebrew": to_script(text, hebrew),
            "Aramaic": to_script(text, aramaic),
            "Greek": to_script(text, greek),
            "Latin": to_script(text, latin)
        }
        for lang, val in translations.items():
            st.markdown(f"<div style='background-color:#FFF5BA; padding:12px; border-radius:12px; font-weight:bold; font-size:20px; margin-bottom:10px'>{lang}: {val}</div>", unsafe_allow_html=True)
    else:
        st.subheader("English (phonetic)")
        translations = {
            "From Brahmi": to_english(text, {v:k for k,v in {**brahmi_cons, **brahmi_indep_vowels}.items()}),
            "From Kharosthi": to_english(text, {v:k for k,v in {**kharosthi_cons, **kharosthi_indep_vowels}.items()}),
            "From Tamil": to_english(text, tamil_rev),
            "From Hebrew": to_english(text, hebrew_rev),
            "From Aramaic": to_english(text, aramaic_rev),
            "From Greek": to_english(text, greek_rev),
            "From Latin": to_english(text, latin_rev)
        }
        for lang, val in translations.items():
            st.markdown(f"<div style='background-color:#B8FFBA; padding:12px; border-radius:12px; font-weight:bold; font-size:20px; margin-bottom:10px'>{lang}: {val}</div>", unsafe_allow_html=True)
