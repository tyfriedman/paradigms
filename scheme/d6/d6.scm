;; scheme daily homework 6
;; name: Ty Friedman
;; date: 9/9/24 

(define (atom? x)
  (and (not (null? x))
       (not (pair? x))))

(define sum*
  (lambda (ttup)
    (cond
	   ((null?  ttup) 0)
      ((atom? (car ttup)) (+ (car ttup) (sum* (cdr ttup))))
      (else (+ (sum* (car ttup)) (sum* (cdr ttup)))))))

;; tests!
(display (sum* '((5)) ))
(display "\n")

(display (sum* '((0) ((0) ((5))) ((0) ((10)))) ))
(display "\n")

(display (sum* '((0) ((0) ((5) ((7)))) ((0) ((10) ))) ))
(display "\n")

(display (sum* '((0) ((0) ((5) ((7) ) ((8) ))) ((0) ((10) ))) ))
(display "\n")

;; correct output:
;;   $ guile d6.scm
;;   5
;;   15
;;   22
;;   30

