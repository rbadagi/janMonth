"""
Specialized Lambda Function Applications
=======================================
Domain-specific and advanced lambda patterns
"""

import json
import re
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from functools import reduce, partial
from operator import itemgetter, attrgetter

# ============================================================================
# DATA SCIENCE & ANALYTICS LAMBDA FUNCTIONS
# ============================================================================

def data_science_lambdas():
    """Lambda functions for data science operations"""
    print("=== DATA SCIENCE LAMBDA FUNCTIONS ===")
    
    # Sample dataset
    sales_data = [
        {'date': '2024-01-01', 'product': 'A', 'sales': 100, 'region': 'North'},
        {'date': '2024-01-02', 'product': 'B', 'sales': 150, 'region': 'South'},
        {'date': '2024-01-03', 'product': 'A', 'sales': 120, 'region': 'North'},
        {'date': '2024-01-04', 'product': 'C', 'sales': 200, 'region': 'East'},
        {'date': '2024-01-05', 'product': 'B', 'sales': 180, 'region': 'South'},
    ]
    
    # Statistical operations using lambda
    total_sales = reduce(lambda acc, item: acc + item['sales'], sales_data, 0)
    avg_sales = total_sales / len(sales_data)
    
    print(f"Total sales: {total_sales}")
    print(f"Average sales: {avg_sales:.2f}")
    
    # Group by operations
    from itertools import groupby
    
    # Group by product
    sorted_by_product = sorted(sales_data, key=lambda x: x['product'])
    product_totals = {
        product: sum(map(lambda x: x['sales'], list(group)))
        for product, group in groupby(sorted_by_product, key=lambda x: x['product'])
    }
    
    print(f"Sales by product: {product_totals}")
    
    # Percentile calculation
    sales_values = list(map(lambda x: x['sales'], sales_data))
    sorted_sales = sorted(sales_values)
    
    percentile = lambda data, p: sorted(data)[int(len(data) * p / 100)]
    
    print(f"50th percentile (median): {percentile(sales_values, 50)}")
    print(f"90th percentile: {percentile(sales_values, 90)}")
    
    # Moving average
    def moving_average(data, window):
        return [
            sum(data[i:i+window]) / window
            for i in range(len(data) - window + 1)
        ]
    
    ma_3 = moving_average(sales_values, 3)
    print(f"3-day moving average: {ma_3}")

def machine_learning_lambdas():
    """Lambda functions for ML preprocessing"""
    print("\n=== MACHINE LEARNING LAMBDA FUNCTIONS ===")
    
    # Feature engineering
    raw_data = [
        {'age': 25, 'income': 50000, 'education': 'Bachelor'},
        {'age': 35, 'income': 75000, 'education': 'Master'},
        {'age': 45, 'income': 90000, 'education': 'PhD'},
        {'age': 30, 'income': 60000, 'education': 'Bachelor'},
    ]
    
    # Normalize age (min-max scaling)
    ages = list(map(lambda x: x['age'], raw_data))
    min_age, max_age = min(ages), max(ages)
    
    normalize_age = lambda age: (age - min_age) / (max_age - min_age)
    
    # One-hot encoding for education
    education_encoder = lambda edu: {
        'edu_bachelor': 1 if edu == 'Bachelor' else 0,
        'edu_master': 1 if edu == 'Master' else 0,
        'edu_phd': 1 if edu == 'PhD' else 0
    }
    
    # Feature engineering pipeline
    processed_data = list(map(
        lambda x: {
            'age_normalized': normalize_age(x['age']),
            'income_log': __import__('math').log(x['income']),
            **education_encoder(x['education'])
        },
        raw_data
    ))
    
    print("Processed ML features:")
    for i, features in enumerate(processed_data):
        print(f"  Sample {i+1}: {features}")

# ============================================================================
# WEB DEVELOPMENT LAMBDA FUNCTIONS
# ============================================================================

def web_development_lambdas():
    """Lambda functions for web development"""
    print("\n=== WEB DEVELOPMENT LAMBDA FUNCTIONS ===")
    
    # URL processing
    urls = [
        'https://api.example.com/users/123',
        'http://website.com/products?category=electronics',
        'https://blog.site.org/posts/2024/01/article',
        'ftp://files.company.net/documents/report.pdf'
    ]
    
    # Extract domains
    extract_domain = lambda url: url.split('//')[1].split('/')[0] if '//' in url else url
    domains = list(map(extract_domain, urls))
    print(f"Extracted domains: {domains}")
    
    # Filter HTTPS URLs
    https_urls = list(filter(lambda url: url.startswith('https://'), urls))
    print(f"HTTPS URLs: {https_urls}")
    
    # HTTP request processing simulation
    requests = [
        {'method': 'GET', 'path': '/api/users', 'status': 200, 'response_time': 0.15},
        {'method': 'POST', 'path': '/api/users', 'status': 201, 'response_time': 0.25},
        {'method': 'GET', 'path': '/api/products', 'status': 404, 'response_time': 0.05},
        {'method': 'PUT', 'path': '/api/users/123', 'status': 200, 'response_time': 0.30},
    ]
    
    # Analyze request patterns
    successful_requests = list(filter(lambda r: 200 <= r['status'] < 300, requests))
    avg_response_time = sum(map(lambda r: r['response_time'], successful_requests)) / len(successful_requests)
    
    print(f"Successful requests: {len(successful_requests)}")
    print(f"Average response time: {avg_response_time:.3f}s")
    
    # Route grouping
    from itertools import groupby
    sorted_by_method = sorted(requests, key=lambda r: r['method'])
    method_groups = {
        method: list(group)
        for method, group in groupby(sorted_by_method, key=lambda r: r['method'])
    }
    
    print("Requests by method:")
    for method, reqs in method_groups.items():
        print(f"  {method}: {len(reqs)} requests")

def api_processing_lambdas():
    """Lambda functions for API data processing"""
    print("\n=== API PROCESSING LAMBDA FUNCTIONS ===")
    
    # JSON API response processing
    api_response = {
        'users': [
            {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'active': True},
            {'id': 2, 'name': 'Bob', 'email': 'bob@example.com', 'active': False},
            {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com', 'active': True},
        ],
        'pagination': {'page': 1, 'total_pages': 5, 'total_users': 50}
    }
    
    # Extract active users
    active_users = list(filter(lambda u: u['active'], api_response['users']))
    print(f"Active users: {[u['name'] for u in active_users]}")
    
    # Transform user data
    user_summary = list(map(
        lambda u: {
            'id': u['id'],
            'display_name': u['name'].upper(),
            'domain': u['email'].split('@')[1]
        },
        active_users
    ))
    
    print("User summary:")
    for user in user_summary:
        print(f"  {user}")
    
    # Pagination helper
    has_next_page = lambda resp: resp['pagination']['page'] < resp['pagination']['total_pages']
    next_page_url = lambda base_url, resp: f"{base_url}?page={resp['pagination']['page'] + 1}"
    
    print(f"Has next page: {has_next_page(api_response)}")
    if has_next_page(api_response):
        print(f"Next page URL: {next_page_url('https://api.example.com/users', api_response)}")

# ============================================================================
# FINANCIAL & BUSINESS LAMBDA FUNCTIONS
# ============================================================================

def financial_lambdas():
    """Lambda functions for financial calculations"""
    print("\n=== FINANCIAL LAMBDA FUNCTIONS ===")
    
    # Portfolio data
    portfolio = [
        {'symbol': 'AAPL', 'shares': 100, 'price': 150.00, 'purchase_price': 140.00},
        {'symbol': 'GOOGL', 'shares': 50, 'price': 2500.00, 'purchase_price': 2400.00},
        {'symbol': 'MSFT', 'shares': 75, 'price': 300.00, 'purchase_price': 320.00},
    ]
    
    # Calculate portfolio metrics
    calculate_value = lambda stock: stock['shares'] * stock['price']
    calculate_gain_loss = lambda stock: (stock['price'] - stock['purchase_price']) * stock['shares']
    calculate_return_pct = lambda stock: ((stock['price'] - stock['purchase_price']) / stock['purchase_price']) * 100
    
    # Apply calculations
    portfolio_with_metrics = list(map(
        lambda stock: {
            **stock,
            'current_value': calculate_value(stock),
            'gain_loss': calculate_gain_loss(stock),
            'return_pct': calculate_return_pct(stock)
        },
        portfolio
    ))
    
    print("Portfolio analysis:")
    for stock in portfolio_with_metrics:
        print(f"  {stock['symbol']}: ${stock['current_value']:.2f} "
              f"({stock['return_pct']:+.1f}%)")
    
    # Portfolio totals
    total_value = sum(map(lambda s: s['current_value'], portfolio_with_metrics))
    total_gain_loss = sum(map(lambda s: s['gain_loss'], portfolio_with_metrics))
    
    print(f"Total portfolio value: ${total_value:.2f}")
    print(f"Total gain/loss: ${total_gain_loss:+.2f}")
    
    # Risk analysis
    returns = list(map(lambda s: s['return_pct'], portfolio_with_metrics))
    avg_return = sum(returns) / len(returns)
    
    # Simple volatility calculation
    variance = sum(map(lambda r: (r - avg_return) ** 2, returns)) / len(returns)
    volatility = variance ** 0.5
    
    print(f"Average return: {avg_return:.2f}%")
    print(f"Volatility: {volatility:.2f}%")

def business_analytics_lambdas():
    """Lambda functions for business analytics"""
    print("\n=== BUSINESS ANALYTICS LAMBDA FUNCTIONS ===")
    
    # Customer data
    customers = [
        {'id': 1, 'name': 'Alice', 'orders': 5, 'total_spent': 500, 'last_order': '2024-01-15'},
        {'id': 2, 'name': 'Bob', 'orders': 2, 'total_spent': 150, 'last_order': '2023-12-20'},
        {'id': 3, 'name': 'Charlie', 'orders': 8, 'total_spent': 1200, 'last_order': '2024-01-20'},
        {'id': 4, 'name': 'Diana', 'orders': 1, 'total_spent': 75, 'last_order': '2023-11-10'},
    ]
    
    # Customer segmentation
    segment_customer = lambda c: (
        'VIP' if c['total_spent'] > 1000 else
        'Regular' if c['total_spent'] > 200 else
        'New'
    )
    
    # Customer lifetime value
    calculate_clv = lambda c: c['total_spent'] / c['orders'] * 12  # Simplified CLV
    
    # Recency analysis
    from datetime import datetime
    
    def days_since_last_order(last_order_str):
        last_order = datetime.strptime(last_order_str, '%Y-%m-%d')
        return (datetime.now() - last_order).days
    
    # Enhanced customer data
    enhanced_customers = list(map(
        lambda c: {
            **c,
            'segment': segment_customer(c),
            'avg_order_value': c['total_spent'] / c['orders'],
            'clv': calculate_clv(c),
            'days_since_last_order': days_since_last_order(c['last_order'])
        },
        customers
    ))
    
    print("Customer analysis:")
    for customer in enhanced_customers:
        print(f"  {customer['name']}: {customer['segment']} "
              f"(CLV: ${customer['clv']:.0f}, AOV: ${customer['avg_order_value']:.2f})")
    
    # Segment analysis
    from itertools import groupby
    
    sorted_by_segment = sorted(enhanced_customers, key=lambda c: c['segment'])
    segment_analysis = {
        segment: {
            'count': len(list(group)),
            'total_value': sum(map(lambda c: c['total_spent'], list(group)))
        }
        for segment, group in groupby(sorted_by_segment, key=lambda c: c['segment'])
    }
    
    print("\nSegment analysis:")
    for segment, metrics in segment_analysis.items():
        print(f"  {segment}: {metrics['count']} customers, ${metrics['total_value']} total value")

# ============================================================================
# TEXT PROCESSING & NLP LAMBDA FUNCTIONS
# ============================================================================

def text_processing_lambdas():
    """Lambda functions for text processing"""
    print("\n=== TEXT PROCESSING LAMBDA FUNCTIONS ===")
    
    # Sample text data
    texts = [
        "Python is a powerful programming language",
        "Lambda functions make code more concise",
        "Data science requires good analytical skills",
        "Machine learning is transforming industries"
    ]
    
    # Text preprocessing
    clean_text = lambda text: re.sub(r'[^\w\s]', '', text.lower())
    tokenize = lambda text: text.split()
    
    # Process texts
    processed_texts = list(map(
        lambda text: tokenize(clean_text(text)),
        texts
    ))
    
    print("Tokenized texts:")
    for i, tokens in enumerate(processed_texts):
        print(f"  Text {i+1}: {tokens}")
    
    # Word frequency analysis
    all_words = [word for tokens in processed_texts for word in tokens]
    word_freq = Counter(all_words)
    
    print(f"\nMost common words: {word_freq.most_common(5)}")
    
    # Text statistics
    text_stats = list(map(
        lambda text: {
            'length': len(text),
            'word_count': len(text.split()),
            'avg_word_length': sum(map(len, text.split())) / len(text.split()),
            'unique_words': len(set(text.lower().split()))
        },
        texts
    ))
    
    print("\nText statistics:")
    for i, stats in enumerate(text_stats):
        print(f"  Text {i+1}: {stats}")

def nlp_lambdas():
    """Lambda functions for NLP tasks"""
    print("\n=== NLP LAMBDA FUNCTIONS ===")
    
    # Sentiment analysis (simplified)
    positive_words = {'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic'}
    negative_words = {'bad', 'terrible', 'awful', 'horrible', 'disappointing', 'poor'}
    
    sentiment_score = lambda text: (
        len([word for word in text.lower().split() if word in positive_words]) -
        len([word for word in text.lower().split() if word in negative_words])
    )
    
    classify_sentiment = lambda score: (
        'positive' if score > 0 else
        'negative' if score < 0 else
        'neutral'
    )
    
    # Sample reviews
    reviews = [
        "This product is amazing and works great!",
        "Terrible quality, very disappointing purchase",
        "It's okay, nothing special but does the job",
        "Excellent service and fantastic results!"
    ]
    
    # Analyze sentiment
    sentiment_analysis = list(map(
        lambda review: {
            'review': review,
            'score': sentiment_score(review),
            'sentiment': classify_sentiment(sentiment_score(review))
        },
        reviews
    ))
    
    print("Sentiment analysis:")
    for analysis in sentiment_analysis:
        print(f"  {analysis['sentiment'].upper()}: {analysis['review']}")
    
    # Text similarity (Jaccard similarity)
    def jaccard_similarity(text1, text2):
        set1 = set(text1.lower().split())
        set2 = set(text2.lower().split())
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return intersection / union if union > 0 else 0
    
    # Find similar texts
    similarity_threshold = 0.2
    similar_pairs = [
        (i, j, jaccard_similarity(reviews[i], reviews[j]))
        for i in range(len(reviews))
        for j in range(i+1, len(reviews))
        if jaccard_similarity(reviews[i], reviews[j]) > similarity_threshold
    ]
    
    print(f"\nSimilar text pairs (threshold > {similarity_threshold}):")
    for i, j, similarity in similar_pairs:
        print(f"  Reviews {i+1} & {j+1}: {similarity:.3f} similarity")

# ============================================================================
# SYSTEM ADMINISTRATION LAMBDA FUNCTIONS
# ============================================================================

def system_admin_lambdas():
    """Lambda functions for system administration"""
    print("\n=== SYSTEM ADMINISTRATION LAMBDA FUNCTIONS ===")
    
    # Log parsing
    log_entries = [
        "2024-01-01 10:00:00 INFO Application started",
        "2024-01-01 10:05:00 ERROR Database connection failed",
        "2024-01-01 10:06:00 WARN Retrying database connection",
        "2024-01-01 10:07:00 INFO Database connection restored",
        "2024-01-01 10:15:00 ERROR Out of memory",
    ]
    
    # Parse log entries
    parse_log = lambda entry: {
        'timestamp': entry[:19],
        'level': entry[20:].split()[0],
        'message': ' '.join(entry[20:].split()[1:])
    }
    
    parsed_logs = list(map(parse_log, log_entries))
    
    # Filter by log level
    error_logs = list(filter(lambda log: log['level'] == 'ERROR', parsed_logs))
    print(f"Error logs: {len(error_logs)}")
    for log in error_logs:
        print(f"  {log['timestamp']}: {log['message']}")
    
    # System metrics simulation
    metrics = [
        {'timestamp': '10:00', 'cpu': 45, 'memory': 60, 'disk': 30},
        {'timestamp': '10:05', 'cpu': 80, 'memory': 75, 'disk': 32},
        {'timestamp': '10:10', 'cpu': 95, 'memory': 85, 'disk': 35},
        {'timestamp': '10:15', 'cpu': 70, 'memory': 70, 'disk': 33},
    ]
    
    # Alert conditions
    cpu_alert = lambda m: m['cpu'] > 90
    memory_alert = lambda m: m['memory'] > 80
    
    # Check for alerts
    alerts = list(filter(
        lambda m: cpu_alert(m) or memory_alert(m),
        metrics
    ))
    
    print(f"\nSystem alerts: {len(alerts)}")
    for alert in alerts:
        conditions = []
        if cpu_alert(alert):
            conditions.append(f"CPU: {alert['cpu']}%")
        if memory_alert(alert):
            conditions.append(f"Memory: {alert['memory']}%")
        print(f"  {alert['timestamp']}: {', '.join(conditions)}")

# ============================================================================
# DEMONSTRATION FUNCTION
# ============================================================================

def run_specialized_examples():
    """Run all specialized lambda examples"""
    data_science_lambdas()
    machine_learning_lambdas()
    web_development_lambdas()
    api_processing_lambdas()
    financial_lambdas()
    business_analytics_lambdas()
    text_processing_lambdas()
    nlp_lambdas()
    system_admin_lambdas()

if __name__ == "__main__":
    run_specialized_examples()
