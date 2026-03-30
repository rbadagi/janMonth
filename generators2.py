#ww
"""
Real-World Python Generator Applications
=======================================
Practical examples for common use cases
"""

import os
import re
import hashlib
from datetime import datetime, timedelta
from typing import Generator, Dict, List, Any

# ============================================================================
# FILE PROCESSING GENERATORS
# ============================================================================

def find_files_by_extension(directory: str, extension: str) -> Generator[str, None, None]:
    """Find all files with specific extension in directory tree"""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                yield os.path.join(root, file)

def duplicate_file_finder(directory: str) -> Generator[Dict[str, List[str]], None, None]:
    """Find duplicate files based on content hash"""
    hash_map = {}
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                
                if file_hash not in hash_map:
                    hash_map[file_hash] = []
                hash_map[file_hash].append(filepath)
            except (IOError, OSError):
                continue
    
    # Yield groups of duplicate files
    for file_hash, file_list in hash_map.items():
        if len(file_list) > 1:
            yield {'hash': file_hash, 'files': file_list}

def large_file_processor(filepath: str, chunk_size: int = 1024*1024) -> Generator[str, None, None]:
    """Process large files in chunks to avoid memory issues"""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

# ============================================================================
# LOG ANALYSIS GENERATORS
# ============================================================================

def apache_log_parser(log_file: str) -> Generator[Dict[str, str], None, None]:
    """Parse Apache access logs"""
    log_pattern = re.compile(
        r'(\S+) \S+ \S+ \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+) (\S+)" (\d{3}) (\d+|-)'
    )
    
    with open(log_file, 'r') as file:
        for line in file:
            match = log_pattern.match(line.strip())
            if match:
                yield {
                    'ip': match.group(1),
                    'timestamp': match.group(2),
                    'method': match.group(3),
                    'url': match.group(4),
                    'protocol': match.group(5),
                    'status': int(match.group(6)),
                    'size': int(match.group(7)) if match.group(7) != '-' else 0
                }

def error_log_analyzer(log_file: str, error_patterns: List[str]) -> Generator[Dict[str, Any], None, None]:
    """Analyze logs for specific error patterns"""
    compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in error_patterns]
    
    with open(log_file, 'r') as file:
        for line_num, line in enumerate(file, 1):
            for pattern_idx, pattern in enumerate(compiled_patterns):
                if pattern.search(line):
                    yield {
                        'line_number': line_num,
                        'pattern_index': pattern_idx,
                        'pattern': error_patterns[pattern_idx],
                        'line_content': line.strip(),
                        'timestamp': datetime.now()
                    }

def log_aggregator(log_file: str, time_window: int = 60) -> Generator[Dict[str, Any], None, None]:
    """Aggregate log entries by time windows"""
    current_window = {}
    window_start = None
    
    for log_entry in apache_log_parser(log_file):
        # Parse timestamp (simplified)
        entry_time = datetime.now()  # In real scenario, parse from log_entry['timestamp']
        
        if window_start is None:
            window_start = entry_time
        
        # Check if we need to start a new window
        if (entry_time - window_start).seconds >= time_window:
            if current_window:
                yield {
                    'window_start': window_start,
                    'window_end': entry_time,
                    'total_requests': sum(current_window.values()),
                    'status_codes': current_window.copy()
                }
            
            current_window = {}
            window_start = entry_time
        
        # Aggregate by status code
        status = log_entry['status']
        current_window[status] = current_window.get(status, 0) + 1

# ============================================================================
# DATA STREAMING GENERATORS
# ============================================================================

def sensor_data_simulator() -> Generator[Dict[str, Any], None, None]:
    """Simulate streaming sensor data"""
    import random
    import time
    
    sensor_id = 1
    while True:
        yield {
            'sensor_id': sensor_id,
            'timestamp': datetime.now().isoformat(),
            'temperature': round(random.uniform(18.0, 25.0), 2),
            'humidity': round(random.uniform(40.0, 70.0), 2),
            'pressure': round(random.uniform(1010.0, 1030.0), 2)
        }
        sensor_id = (sensor_id % 10) + 1
        time.sleep(0.1)  # Simulate real-time data

def moving_average_calculator(data_stream: Generator, window_size: int = 10) -> Generator[float, None, None]:
    """Calculate moving average from data stream"""
    window = []
    
    for value in data_stream:
        # Extract numeric value (assuming it's in 'value' key or is numeric itself)
        if isinstance(value, dict):
            numeric_value = value.get('value', 0)
        else:
            numeric_value = float(value)
        
        window.append(numeric_value)
        
        if len(window) > window_size:
            window.pop(0)
        
        if len(window) == window_size:
            yield sum(window) / len(window)

def anomaly_detector(data_stream: Generator, threshold: float = 2.0) -> Generator[Dict[str, Any], None, None]:
    """Detect anomalies in data stream using simple statistical method"""
    values = []
    
    for data_point in data_stream:
        if isinstance(data_point, dict):
            value = data_point.get('value', 0)
        else:
            value = float(data_point)
        
        values.append(value)
        
        # Need at least 10 points to calculate statistics
        if len(values) >= 10:
            mean = sum(values[-10:]) / 10
            variance = sum((x - mean) ** 2 for x in values[-10:]) / 10
            std_dev = variance ** 0.5
            
            # Check if current value is anomalous
            if abs(value - mean) > threshold * std_dev:
                yield {
                    'timestamp': datetime.now().isoformat(),
                    'value': value,
                    'mean': mean,
                    'std_dev': std_dev,
                    'deviation': abs(value - mean) / std_dev,
                    'anomaly': True
                }

# ============================================================================
# WEB SCRAPING GENERATORS
# ============================================================================

def url_generator(base_urls: List[str], patterns: List[str]) -> Generator[str, None, None]:
    """Generate URLs based on patterns"""
    for base_url in base_urls:
        for pattern in patterns:
            # Simple pattern replacement (in real scenario, use more sophisticated logic)
            for i in range(1, 101):  # Generate 100 URLs per pattern
                url = base_url + pattern.format(page=i, id=i)
                yield url

def html_link_extractor(html_content: str) -> Generator[str, None, None]:
    """Extract all links from HTML content"""
    link_pattern = re.compile(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)
    
    for match in link_pattern.finditer(html_content):
        yield match.group(1)

def sitemap_parser(sitemap_url: str) -> Generator[str, None, None]:
    """Parse XML sitemap and yield URLs"""
    import xml.etree.ElementTree as ET
    import urllib.request
    
    try:
        with urllib.request.urlopen(sitemap_url) as response:
            content = response.read()
        
        root = ET.fromstring(content)
        
        # Handle different sitemap formats
        for url_elem in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
            loc_elem = url_elem.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
            if loc_elem is not None:
                yield loc_elem.text
                
    except Exception as e:
        print(f"Error parsing sitemap: {e}")

# ============================================================================
# DATABASE GENERATORS
# ============================================================================

def database_batch_processor(connection, query: str, batch_size: int = 1000) -> Generator[List[Dict], None, None]:
    """Process database results in batches"""
    cursor = connection.cursor()
    cursor.execute(query)
    
    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
        
        # Convert to list of dictionaries
        columns = [desc[0] for desc in cursor.description]
        batch = [dict(zip(columns, row)) for row in rows]
        yield batch
    
    cursor.close()

def table_sync_generator(source_conn, target_conn, table_name: str, chunk_size: int = 1000):
    """Generate sync operations between two database tables"""
    source_cursor = source_conn.cursor()
    target_cursor = target_conn.cursor()
    
    # Get all IDs from source
    source_cursor.execute(f"SELECT id FROM {table_name} ORDER BY id")
    source_ids = {row[0] for row in source_cursor.fetchall()}
    
    # Get all IDs from target
    target_cursor.execute(f"SELECT id FROM {table_name} ORDER BY id")
    target_ids = {row[0] for row in target_cursor.fetchall()}
    
    # Find differences
    to_insert = source_ids - target_ids
    to_delete = target_ids - source_ids
    
    # Generate insert operations
    for id_batch in [list(to_insert)[i:i+chunk_size] for i in range(0, len(to_insert), chunk_size)]:
        source_cursor.execute(f"SELECT * FROM {table_name} WHERE id IN ({','.join(map(str, id_batch))})")
        rows = source_cursor.fetchall()
        yield {'operation': 'INSERT', 'data': rows}
    
    # Generate delete operations
    for id_batch in [list(to_delete)[i:i+chunk_size] for i in range(0, len(to_delete), chunk_size)]:
        yield {'operation': 'DELETE', 'ids': id_batch}

# ============================================================================
# TESTING AND VALIDATION GENERATORS
# ============================================================================

def test_data_generator(schema: Dict[str, Any], count: int = 100) -> Generator[Dict[str, Any], None, None]:
    """Generate test data based on schema"""
    import random
    import string
    
    for _ in range(count):
        record = {}
        for field, field_type in schema.items():
            if field_type == 'string':
                record[field] = ''.join(random.choices(string.ascii_letters, k=10))
            elif field_type == 'int':
                record[field] = random.randint(1, 1000)
            elif field_type == 'float':
                record[field] = round(random.uniform(0.0, 100.0), 2)
            elif field_type == 'email':
                record[field] = f"user{random.randint(1,1000)}@example.com"
            elif field_type == 'date':
                record[field] = (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat()
        
        yield record

def validation_generator(data_stream: Generator, validators: List[callable]) -> Generator[Dict[str, Any], None, None]:
    """Validate data stream and yield validation results"""
    for item in data_stream:
        validation_result = {
            'data': item,
            'valid': True,
            'errors': []
        }
        
        for validator in validators:
            try:
                if not validator(item):
                    validation_result['valid'] = False
                    validation_result['errors'].append(f"Validation failed: {validator.__name__}")
            except Exception as e:
                validation_result['valid'] = False
                validation_result['errors'].append(f"Validation error: {str(e)}")
        
        yield validation_result

# ============================================================================
# DEMONSTRATION FUNCTIONS
# ============================================================================

def demo_file_processing():
    """Demonstrate file processing generators"""
    print("=== FILE PROCESSING GENERATORS ===")
    
    # Create a sample directory structure for demo
    import tempfile
    import os
    
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some sample files
        for i in range(3):
            with open(os.path.join(temp_dir, f"file{i}.txt"), 'w') as f:
                f.write(f"Content of file {i}")
        
        print(f"Files in {temp_dir}:")
        for file_path in find_files_by_extension(temp_dir, '.txt'):
            print(f"  {file_path}")

def demo_data_streaming():
    """Demonstrate data streaming generators"""
    print("\n=== DATA STREAMING GENERATORS ===")
    
    # Simulate some sensor data
    def sample_data():
        for i in range(10):
            yield {'value': i * 2 + (i % 3)}  # Some pattern with variation
    
    print("Moving average calculation:")
    for avg in moving_average_calculator(sample_data(), window_size=3):
        print(f"  Average: {avg:.2f}")

def demo_test_data():
    """Demonstrate test data generation"""
    print("\n=== TEST DATA GENERATION ===")
    
    schema = {
        'name': 'string',
        'age': 'int',
        'email': 'email',
        'score': 'float'
    }
    
    print("Generated test data:")
    for i, record in enumerate(test_data_generator(schema, 3)):
        print(f"  Record {i+1}: {record}")

if __name__ == "__main__":
    demo_file_processing()
    demo_data_streaming()
    demo_test_data()
