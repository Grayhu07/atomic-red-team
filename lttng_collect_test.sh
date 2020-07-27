lttng create my-kernel-session --output=/tmp/my-kernel-trace
lttng add-context -k -t tid
lttng enable-event --kernel --syscall open,openat,close,read,readv,pread,preadv,write,writev,pwrite,pwritev,clone,fork,execve,accept,connect,recvform,recvmsg,sendto,sendmsg,socket,rename,renameat,chmod,chown,create,pipe,pipe2,setuid,setgid,unlink,unlinkat
lttng enable-event --kernel sched_switch,sched_process_fork,sched_process_free,sched_process_exec,sched_wakeup_new,lttng_statedump_start,lttng_statedump_end,lttng_statedump_process_state,lttng_statedump_file_descriptor
lttng start
