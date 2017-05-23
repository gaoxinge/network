## test

- socket不必先recv，再sendall，两者可以并发

## test1

- inputs不会无限循环
- recv要使用try，否则client中断的时候会报错

## test2

- outputs会无限循环

## test3

- outputs会无限循环，阻塞recv