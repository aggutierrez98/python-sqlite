query_top_products = '''
    SELECT ProductName, SUM(Price * Quantity) as Revenue
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
'''
query_top_employees = '''
    SELECT FirstName || " " || LastName as Employee, COUNT(*) as Total
    FROM Orders o
    JOIN Employees e ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total DESC
    LIMIT 10
'''
query_employee_most_collected = '''
    SELECT FirstName || " " || LastName as Employee, SUM(p.Price * od.Quantity) as Total_Collected
    FROM Orders o
    JOIN Employees e ON e.EmployeeID = o.EmployeeID
    JOIN OrderDetails od ON od.OrderID = o.OrderID
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY o.EmployeeID
    ORDER BY Total_Collected DESC
    LIMIT 1
'''
