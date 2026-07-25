email="Amit_ml@gmail.edu"

def validate_email(email):
    if "@" in email:
        domain = email.split("@")[1]
        if "." in domain:
            return "valid"
    return "invalid"

is_valid = validate_email(email)
if is_valid == "valid":
    print("Valid email address")



def extract_username(email):
    if "@" in email:
        username = email.split("@")[0]
        return username
    return None


def extract_domain(email):
    if "@" in email:
        domain = email.split("@")[1]
        return domain
    return None

def check_domain_ending(email):
    domain = extract_domain(email)
    if domain:
        if domain.endswith(".com"):
            return "Commercial Domain"
        elif domain.endswith(".edu"):
            return "Educational Domain"
        else:
            return "Other Domain"
    return "Invalid Email"





def encode_text(text):
    encoded = ""
    for char in text:
        if char.isalpha() or char == " ":
            encoded += char
    return encoded

def reverse_first_word(text):
    words = text.split()
    if words:
        first_word = words[0]
        reversed_first_word = first_word[::-1]
        return reversed_first_word + " " + " ".join(words[1:])
    return text
def remove_vowels(text):
    vowels = "aeiouAEIOU"
    no_vowels = ""
    reverse_text = reverse_first_word(text)
    second_word = reverse_text.split()[1]
    first_word = reverse_text.split()[0]
    for char in second_word:
        if char not in vowels:
            no_vowels += char
    return first_word + " " + no_vowels

def replace_special_characters(text):
    words = text.split()
    if len(words) > 1:
        second_word = words[1]
        replaced_word = second_word.replace("I", "E").replace("O", "U")
        return words[0] + " " + replaced_word
    return text
def replace_special_characters2(text):
    words = text.split()
    if len(words) > 1:
        second_word = words[1]
        replaced_word = second_word.replace("E", "A").replace("U", "O")
        return words[0] + " " + replaced_word
    return text

########### task 2
print("\nTask 2:")
encoded_text ="###!!@mocleW EPGTQ!!!6789"
encoded_text = encode_text(encoded_text)
print("Encoded Text:", encoded_text)

reversed_text = reverse_first_word(encoded_text)
print("Reversed First Word:", reversed_text)



no_vowels_text = remove_vowels(encoded_text)
print("Text without Vowels:", no_vowels_text)



########## task 3
print("\nTask 3:")
encoded_text = "&&&**$gnirtS PLIO!!@1234"
encoded_text = encode_text(encoded_text)
print("Encoded Text:", encoded_text)
reversed_text = reverse_first_word(encoded_text)
print("Reversed First Word:", reversed_text)
replaced_text = replace_special_characters(reversed_text)
print("Text with Replaced Characters:", replaced_text)



################ task 4
print("\nTask 4:")
encoded_message = "##$$$@!yalpstcejorp EPUVT****9887"
encoded_message = encode_text(encoded_message)
print("Encoded Message:", encoded_message)
reversed_message = reverse_first_word(encoded_message)
print("Reversed First Word:", reversed_message)

replaced_message = replace_special_characters2(reversed_message)
print("Text with Replaced Characters:", replaced_message)