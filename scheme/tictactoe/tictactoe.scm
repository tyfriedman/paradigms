;; scheme tictactoe homework
;; name: Ty Friedman
;; date: 9/19/24

;(load-from-path "/home/scratch/paradigms/scheme_tictactoe/paradigms_ttt.scm")
;(use-modules (ice-9 paradigms_ttt))

; trying a new include mechanism...
(include "paradigms_ttt.scm")

(define (atom? x)
  (and (not (null? x))
       (not (pair? x))))

(define lat?
   (lambda (l) 
      (cond
         ((null? l) #t)
         ((atom? (car l))(lat? (cdr l)))
         (else #f))))
 
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
      ((null? tup) 0)
      ((eq? n (car tup)) 1)
      (else (+ 1 (positionof n (cdr tup)))))))

;; value
;; given a game state, return the value of that state:
;; 10 if it's a win
;; -10 if it's a loss
;; 0 if it is either a draw or not an ending state
(define value
  (lambda (p)
      (lambda (gs)
         (cond
            ((win? p gs) 10)
            ((eq? p 'x) (cond
                           ((win? 'o gs) -10)
                           (else 0)))
            (else (cond 
                  ((win? 'x gs) -10)
                  (else 0)))))))

;; MODIFY your sum* function for this assignment...
(define sum*-g
  (lambda (ttup f)
    (cond
	   ((null?  ttup) 0)
      ((lat? (car ttup)) (+ (f (car ttup)) (sum*-g (cdr ttup) f)))
      (else (+ (sum*-g (car ttup) f) (sum*-g (cdr ttup) f))))))

;; (sum*-g (car (cdr gt)) (value 'o))

;; helper function to return list of values of children
(define childVals
   (lambda (l p)
      (cond
         ((null? l) '())
         (else (cons (sum*-g (car l) (value p)) (childVals (cdr l) p))))))


;; MODIFY this function so that given the game tree 
;; (where the current situation is at the root),
;; it returns the recommendation for the next move
(define nextmove
  (lambda (p gt)
    ;;(pick (positionof (greatest (childVals (cdr gt) p)) (cdr gt)) (childVals (cdr gt) p))))
    (pick (positionof (greatest (childVals (cdr gt) p)) (childVals (cdr gt) p)) (firsts (cdr gt)))))



;; onegametree is defined in paradigms_ttt
;; be sure to look at that file!

;; what is the current game situation?
(display "Current State:     ")
(display (car (onegametree)))
(display "\n")

;; test of nextmove, where should we go next?
(display "Recommended Move:  ")
(display (nextmove 'x (onegametree)))
(display "\n")

;; correct output:
;;   $ guile tictactoe.scm
;;   Current State:     (x o x o o e e x e)
;;   Recommended Move:  (x o x o o x e x e)

