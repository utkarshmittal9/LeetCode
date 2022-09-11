class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visisted_rooms = {0:True}
        def dfs(i):
            for j in i:
                if j not in visisted_rooms:
                    visisted_rooms[j] = True
                    dfs(rooms[j])
                else:
                    continue
        dfs(rooms[0])
        for i in range(len(rooms)):
            if i not in visisted_rooms:
                return False
        return True
                
        
            
        