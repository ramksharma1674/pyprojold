def to_celcius(f):
    celcius = (f - 32) * 5/9
    return celcius

def to_frnh(c):
    frnh = c * 9/5 + 32
    return frnh

def main():
    for temp in range(0, 212, 40):
        print(temp, "Fahrenheit =", round(to_celcius(temp)), "Celcius")
    
    for temp in range(0, 100, 20):
        print(temp, "Celcius =", round(to_frnh(temp)), "Farenheit")
        
if __name__ == "__main__":
    main()            