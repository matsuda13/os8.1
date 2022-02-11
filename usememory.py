d = []
def make_large_list():
    for i in range(2*10**8):
        d.append(i)
    return d
    
def main():
    d = make_large_list()
    result = sum(d)
    print(result)

if __name__ == "__main__":
    main()