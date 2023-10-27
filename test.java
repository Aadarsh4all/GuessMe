class test
{
    int var = 5;

    void fun(){
        var=10;
    }

    public static void main(String[] args) {
        test sc = new test();
        sc.fun();

        System.out.println(sc.var);//?
    }
}
