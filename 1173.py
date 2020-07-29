def main():
    numero = int(input())
    print("N[%d] = %d" %(0, numero))
    for i in range(1, 10):
        numero *= 2
        print("N[%d] = %d" %(i,numero))

if __name__ == "__main__":
    main()