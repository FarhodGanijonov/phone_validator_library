import re

UZB_PHONE_PATTERN = re.compile(
    r'^\+998(33|50|55|77|88|90|91|93|94|95|97|98|99)\d{7}$'
)

def is_valid(phone: str) -> bool:
    """
    O'zbekiston telefon raqamlarini tekshiradi.
    Format: +99890XXXXXXX
    """
    return bool(UZB_PHONE_PATTERN.match(phone))

def normalize(phone: str) -> str:
    """
    Telefon raqamni standart ko‘rinishga (+998XXYYYYYYY) keltiradi.
    Masalan:  '909999999' -> '+998909999999'
    """
    phone = phone.strip().replace(" ", "").replace("-", "")

    if phone.startswith("+998"):
        return phone
    elif phone.startswith("998"):
        return "+" + phone
    elif phone.startswith("0"):
        return "+998" + phone[1:]
    elif len(phone) == 9 and phone.isdigit():
        return "+998" + phone
    else:
        raise ValueError("Telefon raqam noto‘g‘ri formatda")
