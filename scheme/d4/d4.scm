;; scheme daily homework 4
;; name: Ty Friedman
;; date: 9/5/24

(load-from-path "/escnfs/home/tfriedma/esc-courses/fa24-cse-30332.01/public/scheme/d4/paradigms_d4.scm")
(use-modules (ice-9 paradigms_d4))

;; filterN
(define filterN
  (lambda (n m lat)
    (cond 
      ((null? lat) '())
      ((number? (car lat)) (cond
                              ((and (> (car lat) (sub1 n)) (< (car lat) (add1 m))) (cons (car lat) (filterN n m (cdr lat))))
                              (else (filterN n m (cdr lat)))))
      (else (filterN n m (cdr lat))))))
      
    ;; currently this function just returns the lat as it is given
    ;; change the function so that it returns /only/ the numbers
    ;; >= n and <= m
    ;; see below for examples...

;; tests!
(display (filterN 4 6 '(1 turkey 5 9 4 bacon 6 cheese)))
(display "\n")

(display (filterN 4 6 '(4 4 4 1 1 bacon 9 9 8 6 6 6 1 4 5)))
(display "\n")

;; correct output:
;;   $ guile d4.scm
;;   (5 4 6)
;;   (4 4 4 6 6 6 4 5)

