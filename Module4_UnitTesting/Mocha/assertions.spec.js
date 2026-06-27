const {expect} = require("chai");

describe ("Element sum", ()=>{
    let count;

    before(()=>{
        count=[10];
    });

    after(()=>{
        count=null;
    });

    beforeEach(()=>{
        count.push(15);
    });

    afterEach(()=>{
        count.pop();
    });

    it("should be 10,15", ()=>{
        expect(count).to.deep.equal([10,15]);
    });
});