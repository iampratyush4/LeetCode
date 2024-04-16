function memoize(fn) {
  const cache = {};
  let callCount = 0;

  return function(...args) {
    const key = JSON.stringify(args);

    if (cache[key] !== undefined) {
      return cache[key];
    } else {
      const result = fn(...args);
      cache[key] = result;
      callCount=callCount +1 ;
      return result;
    }
  };
}

function sum(a, b) {
  return a + b;
}

function factorial(n) {
  return n <= 1 ? 1 : n * factorial(n - 1);
}

function fib(n) {
  return n <= 1 ? 1 : fib(n - 1) + fib(n - 2);
}

function processActions(fnName, actions, values) {
  const results = [];
  const memoizedFn = memoize(fnName === "sum" ? sum : fnName === "factorial" ? factorial : fib);

  let callCount = 0;

  for (let i = 0; i < actions.length; i++) {
    const action = actions[i];
    const value = values[i];

    if (action === "call") {
      results.push(memoizedFn(...value));
      callCount++;
    } else if (action === "getCallCount") {
      results.push(callCount);
    }
  }

  return results;
}