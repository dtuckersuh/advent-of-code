import fs from 'fs'


fs.readFile('input.txt', 'utf8', (err, data) => {
  if (err) throw err;
  let nums = data.split('\n')
  for (let i = 0; i < nums.length; i++) {
    nums[i] = nums[i].trim()
  }
  const count = nums.reduce((total, curr, index) => {
    curr > nums[index - 1] ? total + 1 : total
    return total;
  })
  console.log(count)
})
