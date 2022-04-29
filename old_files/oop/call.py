class CallMe:
    def __call__(self, *args, **kwargs):
        print('Called:', args, kwargs)

call = CallMe()
call(5,6,7)
call(1,2,3, x = 10, y = 20)