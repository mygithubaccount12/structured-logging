from structured_logging.decorators import instrument_operation, instrument_stage, instrument_function


@instrument_operation("load_data", service="demo_service")
def load_data():
    # Simulate loading data
    return {"records": 42}


@instrument_stage("validate_data", service="demo_service", operation="load_data")
def validate_data(data):
    # Simulate validation logic
    return {"valid": True, "count": data["records"]}


@instrument_function(service="demo_service")
def transform_data(data):
    # Simulate transformation
    return {"transformed": data["records"] * 2}


def main():
    data = load_data()
    validation = validate_data(data)
    transformed = transform_data(data)

    print("Final result:", transformed)


if __name__ == "__main__":
    main()
