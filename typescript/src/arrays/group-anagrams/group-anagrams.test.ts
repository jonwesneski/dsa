import { groupAnagrams } from "./group-anagrams";

test("groupAnagrams basic", () => {
    const result = groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]);
    // Sort groups and inner items to verify match
    // Or just check lengths and membership roughly
    // The result is array of arrays.
    
    // Simplest check for correctness without complex sorting in test:
    // Check if "act" and "cat" are in same group.
    
    const flat = result.flat();
    expect(flat).toContain("act");
    expect(flat).toContain("cat");
    
    // Check grouping logic
    const groupWithAct = result.find(g => g.includes("act"));
    expect(groupWithAct).toContain("cat");
    
    const groupWithPots = result.find(g => g.includes("pots"));
    expect(groupWithPots).toContain("tops");
    expect(groupWithPots).toContain("stop");
});

test("groupAnagrams empty", () => {
    expect(groupAnagrams([""])).toEqual([[""]]);
});
