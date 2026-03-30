# ss
"""
Practical Lambda Function Examples
=================================
Real-world scenarios and common programming tasks
"""

import os
import csv
import json
import sqlite3
from datetime import datetime, timedelta
from collections import defaultdict, namedtuple
from urllib.parse import urlparse, parse_qs

# ============================================================================
# FILE SYSTEM OPERATIONS WITH LAMBDA
# ============================================================================

def file_system_lambdas():
    """Lambda functions for file system operations"""
    print("=== FILE SYSTEM LAMBDA OPERATIONS ===")
    
    # File filtering and processing
    import tempfile
    import os
    
    # Create temporary files for demonstration
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create sample files
        file_data = [
            ('document.txt', 'This is a text document'),
            ('image.jpg', 'fake image data'),
            ('script.py', 'print("Hello World")'),
            ('data.csv', 'name,age\nAlice,25\nBob,30'),
            ('config.json', '{"debug": true}')
        ]
        
        for filename, content in file_data:
            with open(os.path.join(temp_dir, filename), 'w') as f:
                f.write(content)
        
        # Get all files
        all_files = os.listdir(temp_dir)
        
        # Filter files by extension
        get_extension = lambda filename: filename.split('.')[-1] if '.' in filename else ''
        
        # Group files by extension
        files_by_ext = defaultdict(list)
        for file in all_files:
            ext = get_extension(file)
            files_by_ext[ext].append(file)
        
        print("Files grouped by extension:")
        for ext, files in files_by_ext.items():
            print(f"  .{ext}: {files}")
        
        # File size analysis
        get_file_size = lambda filename: os.path.getsize(os.path.join(temp_dir, filename))
        
        file_sizes = list(map(
            lambda f: {'name': f, 'size': get_file_size(f)},
            all_files
        ))
        
        # Sort by size
        sorted_by_size = sorted(file_sizes, key=lambda x: x['size'], reverse=True)
        print("\nFiles sorted by size:")
        for file_info in sorted_by_size:
            print(f"  {file_info['name']}: {file_info['size']} bytes")

def log_analysis_lambdas():
    """Lambda functions for log file analysis"""
    print("\n=== LOG ANALYSIS LAMBDA FUNCTIONS ===")
    
    # Sample log data
    log_lines = [
        "2024-01-01 10:00:00 [INFO] User alice logged in from 192.168.1.100",
        "2024-01-01 10:05:00 [ERROR] Failed login attempt for user bob from 192.168.1.101",
        "2024-01-01 10:10:00 [INFO] User alice accessed /dashboard",
        "2024-01-01 10:15:00 [WARN] High CPU usage detected: 85%",
        "2024-01-01 10:20:00 [ERROR] Database connection timeout",
        "2024-01-01 10:25:00 [INFO] User charlie logged in from 192.168.1.102",
    ]
    
    # Parse log entries
    import re
    
    log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(\w+)\] (.+)')
    
    parse_log_line = lambda line: {
        'timestamp': log_pattern.match(line).group(1),
        'level': log_pattern.match(line).group(2),
        'message': log_pattern.match(line).group(3)
    } if log_pattern.match(line) else None
    
    parsed_logs = list(filter(None, map(parse_log_line, log_lines)))
    
    # Analyze log levels
    log_level_count = defaultdict(int)
    for log in parsed_logs:
        log_level_count[log['level']] += 1
    
    print("Log level distribution:")
    for level, count in log_level_count.items():
        print(f"  {level}: {count}")
    
    # Extract IP addresses from logs
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    
    extract_ips = lambda message: ip_pattern.findall(message)
    
    all_ips = []
    for log in parsed_logs:
        all_ips.extend(extract_ips(log['message']))
    
    ip_frequency = defaultdict(int)
    for ip in all_ips:
        ip_frequency[ip] += 1
    
    print(f"\nIP address frequency: {dict(ip_frequency)}")
    
    # Time-based analysis
    hour_activity = defaultdict(int)
    for log in parsed_logs:
        hour = log['timestamp'].split()[1].split(':')[0]
        hour_activity[hour] += 1
    
    print(f"Activity by hour: {dict(hour_activity)}")

# ============================================================================
# DATA PROCESSING WITH LAMBDA
# ============================================================================

def csv_processing_lambdas():
    """Lambda functions for CSV data processing"""
    print("\n=== CSV PROCESSING LAMBDA FUNCTIONS ===")
    
    # Sample CSV data
    csv_data = [
        {'name': 'Alice', 'age': '25', 'salary': '50000', 'department': 'Engineering'},
        {'name': 'Bob', 'age': '30', 'salary': '60000', 'department': 'Marketing'},
        {'name': 'Charlie', 'age': '35', 'salary': '70000', 'department': 'Engineering'},
        {'name': 'Diana', 'age': '28', 'salary': '55000', 'department': 'Sales'},
        {'name': 'Eve', 'age': '32', 'salary': '65000', 'department': 'Marketing'},
    ]
    
    # Data type conversion
    convert_numeric = lambda value: int(value) if value.isdigit() else float(value) if value.replace('.', '').isdigit() else value
    
    # Convert string numbers to actual numbers
    processed_data = list(map(
        lambda row: {
            key: convert_numeric(value) if key in ['age', 'salary'] else value
            for key, value in row.items()
        },
        csv_data
    ))
    
    print("Processed data with numeric conversion:")
    for row in processed_data[:2]:  # Show first 2 rows
        print(f"  {row}")
    
    # Department analysis
    from itertools import groupby
    
    sorted_by_dept = sorted(processed_data, key=lambda x: x['department'])
    dept_analysis = {}
    for dept, group in groupby(sorted_by_dept, key=lambda x: x['department']):
        group_list = list(group)
        dept_analysis[dept] = {
            'count': len(group_list),
            'avg_salary': sum(map(lambda x: x['salary'], group_list)) / len(group_list),
            'avg_age': sum(map(lambda x: x['age'], group_list)) / len(group_list)
        }
    
    print("\nDepartment analysis:")
    for dept, stats in dept_analysis.items():
        print(f"  {dept}: {stats['count']} employees, "
              f"avg salary: ${stats['avg_salary']:,.0f}, "
              f"avg age: {stats['avg_age']:.1f}")
    
    # Salary bands
    classify_salary = lambda salary: (
        'High' if salary >= 65000 else
        'Medium' if salary >= 55000 else
        'Low'
    )
    
    salary_distribution = defaultdict(int)
    for row in processed_data:
        band = classify_salary(row['salary'])
        salary_distribution[band] += 1
    
    print(f"\nSalary distribution: {dict(salary_distribution)}")

def json_processing_lambdas():
    """Lambda functions for JSON data processing"""
    print("\n=== JSON PROCESSING LAMBDA FUNCTIONS ===")
    
    # Sample JSON data (API response simulation)
    api_data = {
        "users": [
            {
                "id": 1,
                "profile": {
                    "name": "Alice Johnson",
                    "email": "alice@example.com",
                    "preferences": {"theme": "dark", "notifications": True}
                },
                "activity": {
                    "last_login": "2024-01-15T10:30:00Z",
                    "login_count": 45,
                    "posts": 12
                }
            },
            {
                "id": 2,
                "profile": {
                    "name": "Bob Smith",
                    "email": "bob@example.com",
                    "preferences": {"theme": "light", "notifications": False}
                },
                "activity": {
                    "last_login": "2024-01-10T14:20:00Z",
                    "login_count": 23,
                    "posts": 8
                }
            }
        ],
        "metadata": {
            "total_users": 2,
            "active_users": 1,
            "last_updated": "2024-01-15T12:00:00Z"
        }
    }
    
    # Extract nested data
    extract_user_info = lambda user: {
        'id': user['id'],
        'name': user['profile']['name'],
        'email': user['profile']['email'],
        'theme': user['profile']['preferences']['theme'],
        'login_count': user['activity']['login_count'],
        'posts': user['activity']['posts']
    }
    
    flattened_users = list(map(extract_user_info, api_data['users']))
    
    print("Flattened user data:")
    for user in flattened_users:
        print(f"  {user}")
    
    # User engagement score
    calculate_engagement = lambda user: (user['login_count'] * 0.1) + (user['posts'] * 2)
    
    user_engagement = list(map(
        lambda user: {
            **user,
            'engagement_score': calculate_engagement(user)
        },
        flattened_users
    ))
    
    print("\nUser engagement scores:")
    for user in sorted(user_engagement, key=lambda x: x['engagement_score'], reverse=True):
        print(f"  {user['name']}: {user['engagement_score']:.1f}")

# ============================================================================
# DATABASE OPERATIONS WITH LAMBDA
# ============================================================================

def database_lambdas():
    """Lambda functions for database operations"""
    print("\n=== DATABASE LAMBDA FUNCTIONS ===")
    
    # Create in-memory SQLite database for demonstration
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Create sample table
    cursor.execute('''
        CREATE TABLE employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            salary INTEGER,
            hire_date TEXT
        )
    ''')
    
    # Insert sample data
    employees = [
        (1, 'Alice', 'Engineering', 75000, '2022-01-15'),
        (2, 'Bob', 'Marketing', 65000, '2022-03-20'),
        (3, 'Charlie', 'Engineering', 80000, '2021-11-10'),
        (4, 'Diana', 'Sales', 60000, '2023-02-01'),
        (5, 'Eve', 'Marketing', 70000, '2022-08-15'),
    ]
    
    cursor.executemany('INSERT INTO employees VALUES (?, ?, ?, ?, ?)', employees)
    conn.commit()
    
    # Fetch data
    cursor.execute('SELECT * FROM employees')
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    
    # Convert to dictionaries
    dict_rows = list(map(lambda row: dict(zip(columns, row)), rows))
    
    print("Employee data:")
    for emp in dict_rows[:3]:  # Show first 3
        print(f"  {emp}")
    
    # Database analysis using lambda
    # Calculate years of service
    from datetime import datetime
    
    calculate_years_service = lambda hire_date: (
        datetime.now() - datetime.strptime(hire_date, '%Y-%m-%d')
    ).days / 365.25
    
    # Salary analysis
    salary_stats = {
        'min': min(map(lambda emp: emp['salary'], dict_rows)),
        'max': max(map(lambda emp: emp['salary'], dict_rows)),
        'avg': sum(map(lambda emp: emp['salary'], dict_rows)) / len(dict_rows)
    }
    
    print(f"\nSalary statistics: {salary_stats}")
    
    # Department grouping
    from itertools import groupby
    
    sorted_by_dept = sorted(dict_rows, key=lambda x: x['department'])
    dept_stats = {}
    for dept, group in groupby(sorted_by_dept, key=lambda x: x['department']):
        group_list = list(group)
        dept_stats[dept] = {
            'count': len(group_list),
            'total_salary': sum(map(lambda x: x['salary'], group_list))
        }
    
    print("\nDepartment statistics:")
    for dept, stats in dept_stats.items():
        print(f"  {dept}: {stats['count']} employees, "
              f"total salary: ${stats['total_salary']:,}")
    
    conn.close()

# ============================================================================
# WEB SCRAPING & URL PROCESSING WITH LAMBDA
# ============================================================================

def url_processing_lambdas():
    """Lambda functions for URL processing"""
    print("\n=== URL PROCESSING LAMBDA FUNCTIONS ===")
    
    # Sample URLs
    urls = [
        'https://api.example.com/v1/users?page=1&limit=10',
        'http://blog.site.org/posts/2024/python-tips',
        'https://shop.store.com/products/electronics?category=phones&brand=apple',
        'ftp://files.company.net/documents/reports/2024/q1.pdf',
        'https://news.website.com/articles/tech/ai-breakthrough'
    ]
    
    # URL parsing
    parse_url = lambda url: {
        'scheme': urlparse(url).scheme,
        'domain': urlparse(url).netloc,
        'path': urlparse(url).path,
        'query_params': parse_qs(urlparse(url).query)
    }
    
    parsed_urls = list(map(parse_url, urls))
    
    print("Parsed URLs:")
    for i, parsed in enumerate(parsed_urls[:3]):  # Show first 3
        print(f"  URL {i+1}: {parsed}")
    
    # Domain analysis
    domains = list(map(lambda url: urlparse(url).netloc, urls))
    domain_count = defaultdict(int)
    for domain in domains:
        domain_count[domain] += 1
    
    print(f"\nDomain frequency: {dict(domain_count)}")
    
    # Protocol analysis
    protocols = list(map(lambda url: urlparse(url).scheme, urls))
    protocol_count = defaultdict(int)
    for protocol in protocols:
        protocol_count[protocol] += 1
    
    print(f"Protocol distribution: {dict(protocol_count)}")
    
    # Extract file extensions from URLs
    get_file_extension = lambda path: path.split('.')[-1] if '.' in path.split('/')[-1] else None
    
    extensions = list(filter(None, map(
        lambda url: get_file_extension(urlparse(url).path),
        urls
    )))
    
    print(f"File extensions found: {extensions}")

def web_data_processing_lambdas():
    """Lambda functions for web data processing"""
    print("\n=== WEB DATA PROCESSING LAMBDA FUNCTIONS ===")
    
    # Simulate web analytics data
    page_views = [
        {'page': '/home', 'views': 1500, 'bounce_rate': 0.3, 'avg_time': 120},
        {'page': '/products', 'views': 800, 'bounce_rate': 0.4, 'avg_time': 180},
        {'page': '/about', 'views': 300, 'bounce_rate': 0.6, 'avg_time': 90},
        {'page': '/contact', 'views': 150, 'bounce_rate': 0.7, 'avg_time': 60},
        {'page': '/blog', 'views': 600, 'bounce_rate': 0.2, 'avg_time': 240},
    ]
    
    # Calculate engagement metrics
    calculate_engagement = lambda page: (1 - page['bounce_rate']) * page['avg_time'] / 60
    
    # Add engagement score
    enhanced_analytics = list(map(
        lambda page: {
            **page,
            'engagement_score': calculate_engagement(page),
            'views_per_minute': page['views'] / (24 * 60)  # Assuming daily data
        },
        page_views
    ))
    
    print("Page analytics with engagement:")
    for page in sorted(enhanced_analytics, key=lambda x: x['engagement_score'], reverse=True):
        print(f"  {page['page']}: {page['engagement_score']:.2f} engagement, "
              f"{page['views']} views")
    
    # Performance categorization
    categorize_performance = lambda page: (
        'High' if page['views'] > 1000 and page['bounce_rate'] < 0.4 else
        'Medium' if page['views'] > 500 or page['bounce_rate'] < 0.5 else
        'Low'
    )
    
    performance_categories = defaultdict(list)
    for page in enhanced_analytics:
        category = categorize_performance(page)
        performance_categories[category].append(page['page'])
    
    print("\nPage performance categories:")
    for category, pages in performance_categories.items():
        print(f"  {category}: {pages}")

# ============================================================================
# CONFIGURATION & SETTINGS PROCESSING
# ============================================================================

def config_processing_lambdas():
    """Lambda functions for configuration processing"""
    print("\n=== CONFIGURATION PROCESSING LAMBDA FUNCTIONS ===")
    
    # Sample configuration data
    raw_config = {
        'database_url': 'postgresql://user:pass@localhost:5432/mydb',
        'debug_mode': 'true',
        'max_connections': '100',
        'timeout_seconds': '30',
        'feature_flags': 'feature_a,feature_b,feature_c',
        'log_level': 'INFO',
        'cache_ttl': '3600'
    }
    
    # Type conversion functions
    type_converters = {
        'debug_mode': lambda x: x.lower() == 'true',
        'max_connections': lambda x: int(x),
        'timeout_seconds': lambda x: int(x),
        'feature_flags': lambda x: x.split(','),
        'cache_ttl': lambda x: int(x)
    }
    
    # Process configuration
    processed_config = {
        key: type_converters.get(key, lambda x: x)(value)
        for key, value in raw_config.items()
    }
    
    print("Processed configuration:")
    for key, value in processed_config.items():
        print(f"  {key}: {value} ({type(value).__name__})")
    
    # Validation
    validators = {
        'max_connections': lambda x: 1 <= x <= 1000,
        'timeout_seconds': lambda x: 1 <= x <= 300,
        'log_level': lambda x: x in ['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        'cache_ttl': lambda x: x > 0
    }
    
    # Validate configuration
    validation_results = {
        key: validators.get(key, lambda x: True)(processed_config[key])
        for key in processed_config.keys()
    }
    
    print("\nValidation results:")
    for key, is_valid in validation_results.items():
        status = "✓" if is_valid else "✗"
        print(f"  {status} {key}")
    
    # Environment-specific overrides
    env_overrides = {
        'production': {
            'debug_mode': False,
            'log_level': 'WARNING'
        },
        'development': {
            'debug_mode': True,
            'log_level': 'DEBUG'
        }
    }
    
    apply_env_config = lambda base_config, env: {
        **base_config,
        **env_overrides.get(env, {})
    }
    
    prod_config = apply_env_config(processed_config, 'production')
    print(f"\nProduction config debug_mode: {prod_config['debug_mode']}")
    print(f"Production config log_level: {prod_config['log_level']}")

# ============================================================================
# TESTING & VALIDATION WITH LAMBDA
# ============================================================================

def testing_lambdas():
    """Lambda functions for testing and validation"""
    print("\n=== TESTING & VALIDATION LAMBDA FUNCTIONS ===")
    
    # Sample data for validation
    user_data = [
        {'name': 'Alice', 'email': 'alice@example.com', 'age': 25},
        {'name': 'Bob', 'email': 'invalid-email', 'age': 17},
        {'name': '', 'email': 'charlie@example.com', 'age': 30},
        {'name': 'Diana', 'email': 'diana@example.com', 'age': -5},
    ]
    
    # Validation rules
    validators = {
        'name': lambda x: x and len(x.strip()) > 0,
        'email': lambda x: '@' in x and '.' in x.split('@')[-1],
        'age': lambda x: isinstance(x, int) and 18 <= x <= 120
    }
    
    # Validate each user
    validate_user = lambda user: {
        'user': user,
        'valid': all(validators[field](user[field]) for field in validators.keys()),
        'errors': [
            field for field in validators.keys()
            if not validators[field](user[field])
        ]
    }
    
    validation_results = list(map(validate_user, user_data))
    
    print("User validation results:")
    for result in validation_results:
        status = "✓" if result['valid'] else "✗"
        errors_text = f"Errors: {result['errors']}" if not result['valid'] else "Valid"
        print(f"  {status} {result['user']['name'] or 'Unknown'}: {errors_text}")
    
    # Test data generation
    import random
    import string
    
    generate_test_email = lambda: f"test{''.join(random.choices(string.ascii_lowercase, k=5))}@example.com"
    generate_test_name = lambda: ''.join(random.choices(string.ascii_uppercase, k=1)) + ''.join(random.choices(string.ascii_lowercase, k=random.randint(4, 8)))
    
    # Generate test users
    test_users = [
        {
            'name': generate_test_name(),
            'email': generate_test_email(),
            'age': random.randint(18, 65)
        }
        for _ in range(3)
    ]
    
    print("\nGenerated test users:")
    for user in test_users:
        print(f"  {user}")

# ============================================================================
# DEMONSTRATION FUNCTION
# ============================================================================

def run_practical_examples():
    """Run all practical lambda examples"""
    file_system_lambdas()
    log_analysis_lambdas()
    csv_processing_lambdas()
    json_processing_lambdas()
    database_lambdas()
    url_processing_lambdas()
    web_data_processing_lambdas()
    config_processing_lambdas()
    testing_lambdas()

if __name__ == "__main__":
    run_practical_examples()
