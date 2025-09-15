def number_to_words(n):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
            "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if n == 0:
        return "Zero"
    elif n < 20:
        return ones[n]
    elif n < 100:
        return tens[n // 10] + (" " + ones[n % 10] if n % 10 else "")
    elif n < 1000:
        return ones[n // 100] + " Hundred" + (" " + number_to_words(n % 100) if n % 100 else "")
    else:
        return ones[n // 1000] + " Thousand" + (" " + number_to_words(n % 1000) if n % 1000 else "")


# Input
num = int(input("Enter a number: "))
print("In words:", number_to_words(num))
