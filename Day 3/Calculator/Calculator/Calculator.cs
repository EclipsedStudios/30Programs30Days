using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calculator
{
    public enum Mode
    {
        Add,
        Sub,
        Mult,
        Divi,
        None
    }

    public partial class Calculator : Form
    {
        public Mode mode = Mode.None;
        public bool Solved = false;
        public string CurrentInput = "";
        public Calculator()
        {
            InitializeComponent();
        }

        public void UpdateTextbox(string text)
        {
            textBox1.Text = text;
        }

        public void AddToInput(string text)
        {
            if (Solved && !(text.Equals("-") || text.Equals("+") || text.Equals("*") || text.Equals("/")))
            {
                UpdateTextbox("");
                CurrentInput = "";
                mode = Mode.None;
            }

            Solved = false;


            if (CurrentInput.Equals(""))
            {
                if (!text.Equals("0"))
                {
                    CurrentInput = text;
                }
            } else
            {
                CurrentInput += text;
            }
            UpdateTextbox(CurrentInput);
        }


        public void SolveIt(string input)
        {
            string[] split = new string[0];
            double output = 0;
            switch (mode)
            {
                case Mode.Add:
                    split = input.Split('+');
                    output = Double.Parse(split[0]) + Double.Parse(split[1]);
                    UpdateTextbox(output.ToString());
                    break;
                case Mode.Mult:
                    split = input.Split('*');
                    output = Double.Parse(split[0]) * Double.Parse(split[1]);
                    UpdateTextbox(output.ToString());
                    break;
                case Mode.Divi:
                    split = input.Split('/');
                    output = Double.Parse(split[0]) / Double.Parse(split[1]);
                    UpdateTextbox(output.ToString());
                    break;
                case Mode.Sub:
                    split = input.Split('-');
                    output = Double.Parse(split[0]) - Double.Parse(split[1]);
                    UpdateTextbox(output.ToString());
                    break;
                case Mode.None:
                    UpdateTextbox(input);
                break;
            }
            CurrentInput = output.ToString();
            Solved = true;
        }
        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {
            AddToInput("0");
        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {
            AddToInput("1");
        }

        private void button9_Click(object sender, EventArgs e)
        {
            AddToInput("2");
        }

        private void button8_Click(object sender, EventArgs e)
        {
            AddToInput("3");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            AddToInput("4");
        }

        private void button10_Click(object sender, EventArgs e)
        {
            AddToInput("5");
        }

        private void button7_Click(object sender, EventArgs e)
        {
            AddToInput("6");
        }

        

        private void button2_Click(object sender, EventArgs e)
        {
            AddToInput("7");
        }

        private void button11_Click(object sender, EventArgs e)
        {
            AddToInput("8");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            AddToInput("9");
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (mode != Mode.None)
            {
                SolveIt(CurrentInput);
            }
            AddToInput("*");
            mode = Mode.Mult;
        }

        private void button13_Click(object sender, EventArgs e)
        {
            if (mode != Mode.None)
            {
                SolveIt(CurrentInput);
            }
            AddToInput("/");
            mode = Mode.Divi;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            if (mode == Mode.Add)
            {
                SolveIt(CurrentInput);
            }
            AddToInput("+");
            mode = Mode.Add;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (mode != Mode.None)
            {
                SolveIt(CurrentInput);
            }
            AddToInput("-");
            mode = Mode.Sub;
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //Clear
            UpdateTextbox("");
            CurrentInput = "";
            mode = Mode.None;
            Solved = true;
        }

        private void button15_Click_1(object sender, EventArgs e)
        {
            SolveIt(CurrentInput);
        }
    }
}
