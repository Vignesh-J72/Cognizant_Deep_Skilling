describe("Math examples", ()=>{
  let count;

  beforeEach(()=>{
    count=10; 
  });

  test('should add 5 to count', ()=>{
    count=count+5;
    expect(count).toBe(15);
  });

  test('should subtract 2 from count', ()=>{
    count=count-2;
    expect(count).toBe(8);
  });
});