from flask import request
from flask_restful import Resource
from src.controllers.supplier_controller import SupplierController

class SupplierResource(Resource):
    def post(self):
        """
                Add a new Supplier
                ---
                tags:
                  - Suppliers
                parameters:
                  - in: body
                    name: body
                    schema:
                      type: object
                      required:
                        - supplier_name
                        - contact_number
                      properties:
                        supplier_name:
                          type: string
                          description: The name of the supplier
                        contact_number:
                          type: string
                          description: Contact details of the supplier
                responses:
                  201:
                    description: Supplier added successfully!
                  400:
                    description: Supplier already exists
                  500:
                    description: Internal server error
        """
        try:
            # Extract data from request body
            data = request.get_json()

            # Call the controller to add supplier
            result, status_code = SupplierController.add_supplier(data)

            # Return the response from the controller
            return result, status_code

        except Exception as e:
            return {"message": f"Failed to add supplier: {str(e)}"}, 500

    @staticmethod
    def get():
        """
        Get All Suppliers
        ---
        tags:
          - Suppliers
        responses:
          200:
            description: Successfully fetched all Suppliers
          500:
            description: Error fetching Suppliers
        """
        return SupplierController.get_all_supplier()