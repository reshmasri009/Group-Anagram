
def group_anagrams(strs):
    groups = {}  
    
    for word in strs:
        
        signature = ''.join(sorted(word))
        
        
        if signature not in groups:
            groups[signature] = []
        
        
        groups[signature].append(word)
        
        
        print(f"Word: {word}, Signature: {signature}, Groups: {groups}")
    
    
    return list(groups.values())



strs = input("Enter words separated by space: ").split()

result = group_anagrams(strs)
print("\nFinal Grouped Anagrams:")
print(result)
