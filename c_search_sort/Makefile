CC = gcc  # C compiler
CFLAGS = -fPIC -Wall -Wextra -O3  # C flags
LDFLAGS = -shared   # linking flags
RM = rm -f   # rm command
TARGET_LIB = _c_search.so  # target lib

SRCS = _c_search.c  # source files
OBJS = $(SRCS:.c=.o)

.PHONY: all
all: ${TARGET_LIB}

$(TARGET_LIB): $(OBJS)
	$(CC) ${LDFLAGS} -o $@ $^


.PHONY: clean
clean:
	-${RM} ${OBJS}