class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_ptr = len(s) - 1
        t_ptr = len(t) - 1

        s_bs = 0
        t_bs = 0
        while s_ptr >= 0 or t_ptr >= 0:
            while s_ptr >= 0:  # delete valid chars after `#`
                if s[s_ptr] == "#":
                    s_bs += 1
                    s_ptr -= 1
                elif s_bs > 0:
                    s_bs -= 1
                    s_ptr -= 1
                else:
                    break

            while t_ptr >= 0:
                if t[t_ptr] == "#":
                    t_bs += 1
                    t_ptr -= 1
                elif t_bs > 0:
                    t_bs -= 1
                    t_ptr -= 1
                else:
                    break

            if s_ptr >= 0 and t_ptr >= 0 and s[s_ptr] != t[t_ptr]:  # compare
                return False

            if (s_ptr >= 0 and not t_ptr >= 0) or (
                not s_ptr >= 0 and t_ptr >= 0
            ):  # if we end up checking correct chars
                return False

            s_ptr -= 1
            t_ptr -= 1

        return True
