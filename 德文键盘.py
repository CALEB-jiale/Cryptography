import hashlib
import itertools
# (Q=win*5


def is_equal(c):
    return hashlib.sha1(c.encode('utf8')).hexdigest() == '67ae1a64661ac8b4494666f58c4822408dd0a3e4'


def main():
    k = '(Q=Win5qw80IN*%'
    for i in range(4, 10):
        keys = itertools.permutations(k, i)
        for key in keys:
            c = ''.join(key)
            if is_equal(c):
                print(c)
                return


if __name__ == '__main__':
    main()
