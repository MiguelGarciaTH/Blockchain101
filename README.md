Blockchain101 is a Summer School course on Blockchain technology.
In this page I will make available all the slides and code.

# What you will learn
This course is an hands-on introduction to Blockchain technology.

## Table of contents <a name="table"></a>
1. [Security Fundamental Concepts](#intro) (15 September'20 | 5PM-20PM)
2. [Secure Distributed Systems](#distributed_systems) (16 September'20 | 5PM-20PM)
3. [Blockchain in a Nutshell](#blockchain) (17 September'20 | 5PM-20PM)
4. [Assembling the pieces: Blockchain prototype](#prototype) (18 September'20 |  5PM-20PM)



# 1. Security Fundamental Concepts <a name="intro"></a>
---
**Class overview:**

In this class, we will present the course agenda and cover the fundamental concepts of security.
To understand what is a blockchain, one must understand the security properties and how it is possible to implement them.
In particular, we will talk about cryptography which is the core of a blockchain solution.


The students will implement mechanisms as separate modules that provide cryptographic functionalities.


| [Slides](https://github.com/MiguelGarciaTH/Blockchain101/blob/master/slides/1_blockchain101_security_fundamental_concepts.pdf)      | [Code](https://github.com/MiguelGarciaTH/Blockchain101/blob/master/code/module1)       |

---

**Aditional material/References:**
- Slide 12: [Mono-alphabetic Substitution](https://www.dcode.fr/monoalphabetic-substitution)
- Slide 40: [Extended Euclidean Algorithm and Inverse Modulo Tutorial](https://www.youtube.com/watch?time_continue=211&v=fz1vxq5ts5I&feature=emb_logo)
- Slide 50: [SHA-256 hash calculator](https://xorbin.com/tools/sha256-hash-calculator)
- Slide 53 [Computerphile: Hashing Algorithms and Security](https://www.youtube.com/watch?v=b4b8ktEV4Bg)
- Slide 54-63: [Breaking Down: SHA-256 Algorithm](https://medium.com/bugbountywriteup/breaking-down-sha-256-algorithm-2ce61d86f7a3)

- [Eddie Woo: The RSA Encryption Algorithm](https://www.youtube.com/watch?v=4zahvcJ9glg)
- [R. L. Rivest, A. Shamir L. Adleman: A method for obtaining digital signatures and public-key cryptosystems](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjUw5Ptq97qAhVqCWMBHdr4BAwQFjABegQIARAB&url=https%3A%2F%2Fpeople.csail.mit.edu%2Frivest%2FRsapaper.pdf&usg=AOvVaw1FtI2T7P32pKAb6jnZSqxi)
[3Blue1Brown: How secure is 256 bit security?](https://www.youtube.com/watch?v=S9JGmA5_unY)
- [Learning Python](https://www.learnpython.org/en/Hello,_World!)
- [Python Documentation: Hashlib](https://docs.python.org/3/library/hashlib.html)
- [SHA256 user implementation](https://bitbucket.org/pypy/pypy/raw/202f38624d212c87263b5850532ab0573928037f/lib_pypy/_sha256.py), it seems to have problems when running, but it is good to have a look on the SHA256's code.
- [RSA user implementation](https://repl.it/@billbuchanan/rsasig#main.py)

| [top](#table) |


# 2. Secure Distributed Systems <a name="distributed_systems"></a>
---
**Class overview:**

In this class, we will introduce distributed systems.
We will start with a motivational example of a two-person game that is a human-distributed system.
The goal is to understand the security problems of implementing such a system in practice.


The students will implement this game in software using the last class implemented modules.



| [Slides](https://github.com/MiguelGarciaTH/Blockchain101/blob/master/slides/2_blockchain101_secure_distributed_systems.pdf)      | [Code](https://github.com/MiguelGarciaTH/Blockchain101/tree/master/code/module2)       |

---

**Aditional material/References:**
- [A Thorough Introduction to Distributed Systems](https://www.freecodecamp.org/news/a-thorough-introduction-to-distributed-systems-3b91562c9b3c/)
- [Python sockets](https://realpython.com/python-sockets/)
- [Python AES Crypto](https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html)


| [top](#table) |

# 3. Blockchain in a Nutshell <a name="blockchain"></a>
---
**Class overview:**

In this class, we finally introduce Blockchain technology: What it is? What is solves?
We will cover three types of Consensus - which is one of the problems of distributed systems:
- Byzantine Fault Tolerance (BFT);
- Proof-of-Work (PoW);
- Proof-of-Stake (PoS).
Then, we will focus on the first Blockchain that appeared: The Bitcoin.
Bitcoin address the double-spending problem.


The students will implement a PoW system using the knowledge and code implemented in the previous classes.


| [Slides](https://github.com/MiguelGarciaTH/Blockchain101/blob/master/slides/1_blockchain101_security_fundamental_concepts.pdf)      | [Code](https://github.com/MiguelGarciaTH/Blockchain101/blob/master/code/module3)       |

---

**Aditional material/References:**

| [top](#table) |

# 4. Assembling the pieces: Blockchain prototype <a name="prototype"></a>
---
**Class overview:**

In this class we will put all the pieces together and build a blockchain prototype.

The prototype should have:
- Blockchain structure
- Add new blocks
- Mine blocks (PoW algorithm)
- Send blocks to other nodes


| [Slides](https://github.com/MiguelGarciaTH/Blockchain101/blob/master/slides/1_blockchain101_security_fundamental_concepts.pdf)      | [Code](https://github.com/MiguelGarciaTH/Blockchain101/tree/master/code/module4)       |

---

**Aditional material/References:**

| [top](#table) |
