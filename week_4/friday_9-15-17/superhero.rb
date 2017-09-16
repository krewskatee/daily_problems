class Superhero
  attr_reader :name, :hitpoints, :attack, :alive, :has_special_tool
  attr_writer :hitpoints, :attack

  def initialize(input_options)
    @name = input_options[:name]
    @hitpoints = input_options[:hitpoints]
    @attack = input_options[:attack]
    @alive = true
    @has_special_tool = false
  end

  def grab_tool
    @has_special_tool = true
    @attack *= 3
  end

  def alive
    if hitpoints < 1
      return false
    else
      return true
    end
  end

  def hit(superhero)
    superhero.hitpoints -= attack
  end

end
