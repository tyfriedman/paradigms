package main

import (
  "bufio"
  "fmt"
  "sync"
  "os"
)

type hashval struct {
    hash uint32
    str string
}

func djb2Hash(input string) hashval {
  var hash uint32 = 5381
  for _, c := range input {
    hash = ((hash << 5) + hash) + uint32(c)
  }

  hv := hashval{hash: hash, str: input}
  
  return hv
}

func worker(id int, tasks <-chan string, results chan<- hashval, wg *sync.WaitGroup) {
  // now write a worker thread like we did in class
  // your worker should read a string from the tasks channel, call the 
  // djb2Hash kernel with the string, then write the hashval object from
  // djb2Hash to the results channel
  
  for input := range tasks {
    fmt.Printf("worker %d processing task: %s\n", id, input)
    results <- djb2Hash(input)
  }

  wg.Done()
}

func main() {
  const numWorkers = 5

  filename := "random_strings.txt"

  // prepare by opening the filename above as a file object
  file, err := os.Open(filename)
  if err != nil {
    fmt.Println("Error opening file:", err)
    return
  }
  // first make the channels and waitgroup
  tasks := make(chan string)
  results := make(chan hashval)

  var wg sync.WaitGroup

  // second create the workers
  for i := 0; i < numWorkers; i++ {
    wg.Add(1)
    go worker(i, tasks, results, &wg)
  }

  // third create an anomymous goroutine that reads from a file and
  // adds each line to the tasks channel
  // you can use a scanner object to read from the file that is
  // opened above (just look up bufio scanners on Google or ChatGPT)
  go func() {
    scanner := bufio.NewScanner(file)
    for scanner.Scan() {
      tasks <- scanner.Text()
    }
    close(tasks)
  } ()

  // fourth create an anonymous goroutine that waits for the
  // waitgroup and closes the results channel
  go func() {
    wg.Wait()
    close(results)
  } ()

  // fifth process the results by displaying them
  for result := range results {
    fmt.Printf("result: %d\t%s\n", result.hash, result.str)
  }
}

