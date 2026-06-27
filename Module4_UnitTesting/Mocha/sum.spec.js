const { expect, assert } = require('chai');

describe('Test sum', () => {
  it('should add two numbers correctly', () => {
    const result = 2 + 3;
    
    expect(result).to.equal(5);
    expect(result).to.be.a('number');
  });
});

describe("add()", function () {
  let dynamicTests = [];
  before(async function () {
    this.timeout(6000); 

    dynamicTests=await new Promise((resolve)=>{
      setTimeout(resolve, 5000, [
        { args: [1, 2], expected: 3 },
        { args: [1, 2, 3], expected: 6 },
        { args: [1, 2, 3, 4], expected: 10 },
      ]);
    });
  });

  it("correctly adds args for all test vectors",function(){
    dynamicTests.forEach(({ args, expected })=>{
      const res=args.reduce((sum, curr)=>sum+curr, 0);
      assert.strictEqual(res, expected, "Failed adding");
    });
  });
});