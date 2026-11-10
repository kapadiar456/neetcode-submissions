class DynamicArray {
public:
    int * arr;
    int length;
    int capacity;
    DynamicArray(int capacity): length(0), capacity(capacity) {
        arr = new int[capacity];
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (capacity == length)
        {
            resize();
        }  
            arr[length]=n;
            length++;
    }

    int popback() {
        if (length>0)
        {
            length--;
        }
        return arr[length];
    }

    void resize() {
        capacity = capacity*2;
        int * arr2 = new int[capacity];
        for (int i=0; i<length; i++)
        {
            arr2[i]=arr[i]; 
        }
        delete [] arr;
        arr = arr2;
    }

    int getSize() {
        return length;
    }

    int getCapacity() {
        return capacity;
    }
};
