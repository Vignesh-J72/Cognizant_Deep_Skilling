test("Mocks example usage", ()=>{
    const function1 = jest.fn().mockReturnValue("Hello world");

    expect(function1()).toBe("Hello world");
    expect(function1).toHaveBeenCalled();
});