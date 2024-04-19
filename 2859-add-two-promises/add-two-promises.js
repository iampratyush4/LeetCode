/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    try {
        // Wait for both promises to resolve
        const result1 = await promise1;
        const result2 = await promise2;
        
        // Return the sum of the resolved values
        return result1 + result2;
    } catch (error) {
        // Handle any errors
        throw error;
    }
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */