;; scheme daily homework 7
;; name: Ty Friedman
;; date: 9/16/24

(load-from-path "/escnfs/home/tfriedma/esc-courses/fa24-cse-30332.01/public/scheme/d7/paradigms_d7.scm")
(use-modules (ice-9 paradigms_d7))

;; greatest
;; return the greatest value in a tup, e.g., (1 3 2) -> 3
(define greatest
  (lambda (tup)
    (cond
      ((null? tup) 0)
      ((> (car tup) (greatest (cdr tup))) (car tup))
      (else (greatest (cdr tup))))))

;; positionof
;; you may assume that the given tup actually contains n
;; e.g., (positionof 23 (1 52 23 9)) -> 3
(define positionof
  (lambda (n tup)
    (cond
      ((eq? n (car tup)) 1)
      (else (+ 1 (positionof n (cdr tup)))))))

;; value
;; given a game state, return the value of that state:
;; 10 if it's a win
;; -10 if it's a loss
;; 0 if it is either a draw or not an ending state
(define value
  (lambda (p gs)
    (cond
      ((win? p gs) 10)
      ((eq? p 'x) (cond
                     ((win? 'o gs) -10)
                     (else 0)))
      (else (cond 
               ((win? 'x gs) -10)
               (else 0))))))

;; tests for greatest
(display (greatest '(1 9 2)))
(display "\n")

(display (greatest '(143 8 31324 24)))
(display "\n")

;; tests for positionof
(display (positionof 23 '(1 52 23 9)))
(display "\n")

(display (positionof 50 '(50 45 1 52 23 9 102)))
(display "\n")

;; tests for value
(display (value 'x '(x o e o x e e e x)))
(display "\n")

(display (value 'x '(o o o x x e e e e)))
(display "\n")

(display (value 'x '(o o e x x e e e e)))
(display "\n")

;; correct output:
;;   $ guile d7.scm
;;   9
;;   31324
;;   3
;;   1
;;   10
;;   -10
;;   0

