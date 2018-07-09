//
//  ViewController.swift
//  LinearRegression
//
//  Created by Karthik on 08/07/2018.
//  Copyright © 2018 karthik. All rights reserved.
//

import UIKit
import CoreML

class ViewController: UIViewController, UITextFieldDelegate {

    @IBOutlet weak var inputTxtFld: UITextField!
    @IBOutlet weak var resultLbl: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.title = "Salary Vs Experience"
        self.resultLbl.text = ""
        self.inputTxtFld.addTarget(self, action: #selector(textFieldDidChange(_:)), for: .editingChanged)
    }

    //MARK: - UITextFieldDelegate
    
    @objc func textFieldDidChange(_ textField: UITextField) {
        if textField.text == "" {
            self.resultLbl.text = ""
        } else {
            self.findSalary()
        }
    }
    
    //MARK: - Methods
    
    fileprivate func findSalary() {
        if let yearsOfExperience = Double(self.inputTxtFld.text ?? "0") {
            let regressor = SalaryVsExperience()
            do {
                let result = try regressor.prediction(input: yearsOfExperience)
                self.resultLbl.text = "Salary - " + "\(Int(result.prediction))"
                return
            } catch {
            }
        }
        self.resultLbl.text = ""
    }
    
}

