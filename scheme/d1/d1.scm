;; this is how to load external modules in scheme
(load-from-path "/escnfs/home/tfriedma/esc-courses/fa24-cse-30332.01/public/scheme/d1/paradigms_d1.scm")
(use-modules (ice-9 paradigms_d1))

;; Ty Friedman

;; the list q
;; notice it has a ' in front of the list; that tells the interpreter to read
;; the list literally (e.g., as atoms, instead of functions)
(define q '(turkey (gravy) (stuffing potatoes ham) peas))

;; question 1
(display "question 1: ")
(display (atom? (car (cdr (cdr q)))))
(display "\n")
;; output:
;; #f
;; 
;; explanation:
;; the most inside cdr q leaves us with ((gravy) (stuffing potatoes ham) peas)
;; the next cdr leaves us with ((stuffing potatoes ham) peas)
;; the car leaves us with (stuffing potatoes ham), which is not an atom becasue it is a list
;; thus, the statement evaluates to #f


;; question 2
(display "question 2: ")
(display (lat? (car (cdr (cdr q)))))
(display "\n")
;; output:
;; #t
;;
;; explanation:
;; the (car (cdr (cdr q))) leaves us with the same thing that we were left with above, which is (stuffing, potatoes, ham)
;; this is a list of atoms, so lat? evaluates to #t


;; question 3
(display "question 3: ")
(display (cond ((atom? (car q)) (car q)) (else '())))
(display "\n")
;; output:
;; turkey
;;
;; explanation:
;; the first statement in the conditional, (car q) is turkey, which is an atom
;; thus the conditional ends at the first statement and the value of the first conditional is what the statement evaluates to
;; therefore, the statement evaluates to (car q), which is turkey

