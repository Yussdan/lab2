function testTask(done) {
  console.log(`1+1=${1+1}`);
  done();
}

exports.test = testTask;